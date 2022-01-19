from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QInputDialog, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QObject
from PyQt5.QtGui import QPixmap
import sys
from gui import Ui_Display
from libbeep import Beeper
from bluetooth_utility import BLE
import traceback 
import bluetooth
import time
# import gpiozero

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
# GPIO.output(13, GPIO.LOW)


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data
    
    error
        `tuple` (exctype, value, traceback.format_exc() )
    
    result
        `object` data returned from processing, anything    
    
    progress
        `int` to show the progress
    
    info
        `str` to show the messages or update about the procress

    '''
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
    info = pyqtSignal(str)
    
    
class BluetoothWorker(QThread):
    signals = WorkerSignals()
    

    def __init__(self, parent=None):
        super(BluetoothWorker, self).__init__(parent)

        self.threadactive = True
        
        while True:
            try:
                self.BLE = BLE(asQthread= True)
                self.MAC_ADD = 'B4:E6:2D:B3:0B:1B'
                self.threadactive = self.BLE.select_device(self.MAC_ADD)   
                if self.threadactive:
                    break
            except:
                QThread.sleep(1) 

        
    @QtCore.pyqtSlot()
    def run(self,):
        
        # self.beeper = Beeper(asQthread=False)
        # beepsetup()
        # beepoff()
        
        self.results = None
        self.alarm = False
        # emit the signal first time to confirm the connection
        self.signals.result.emit(self.alarm)
        # GPIO.setmode(GPIO.BOARD)
        # # BuzzerPin 7
        # GPIO.setup(7, GPIO.OUT)
        # GPIO.output(7, GPIO.LOW)
        # buzzer = gpiozero.LED(7)
        while self.threadactive:
            
            msg = self.BLE.read(2)
            msg =int(msg)
            print(msg)
            # beep = False
            
            if msg == 5 or self.alarm:
                self.alarm = True
                
                 
            if msg != 5:
                # self.beeper.off()
                self.alarm = False
                
            self.signals.result.emit(self.alarm)

            
            # QThread.sleep(1)
            
        try:
            self.BLE.stop()
            #close bluetooh
            print('Succesfully closed Bluetooth')
            self.signals.info.emit('Closed')
        except:
            print('Error closing Bluetooth')
            self.signals.info.emit('Failed')
            
        self.signals.finished.emit()
        
    def stop(self):
        self.threadactive = False

class BeepWorker(QThread):
    signals = WorkerSignals()
    
    def __init__(self, parent=None):
        super(BeepWorker, self).__init__(parent)
        self.threadactive = True
        self.on_flag = False
        
    @QtCore.pyqtSlot()
    def run(self,):
        
        while self.threadactive:
            # print('beeP FLAG', self.on_flag)
            if self.on_flag:
                print('beeping')
                GPIO.output(37, GPIO.HIGH)
                QThread.msleep(300) # sleep for one seconds. this only accepts integer
                GPIO.output(37, GPIO.LOW)
                self.on_flag ^= True
            QThread.msleep(300)
                
    def turn_on(self,):
        print('Here')
        self.on_flag = True
        
    def stop(self):
        self.threadactive = False

class ClockWorker(QThread):
    signals = WorkerSignals()
    
    def __init__(self, parent=None):
        super(ClockWorker, self).__init__(parent)
        
        self.threadactive = True
        
    @QtCore.pyqtSlot()
    def run(self,):
        
        while self.threadactive:
            #emit a signal every second to update the clock
            self.signals.result.emit(True)
            QThread.sleep(1) # sleep for one seconds. this only accepts integer
        
    def stop(self):
        self.threadactive = False

class MyWindow(QtWidgets.QMainWindow, Ui_Display):
    def __init__(self):
        
        '''Intial UI setup'''
        QtWidgets.QMainWindow.__init__(self)
        Ui_Display.__init__(self)
        self.ui = Ui_Display()
        self.ui.setupUi(self)       
        #set the scaling for label
        self.ui.label.setScaledContents(True)
        # load all the images at begining this will increase RAM but will speedup the processing time
        self.ble_search = QPixmap("bluetooth_search.png")
        self.ble_connect = QPixmap("bluetooth.png")
        self.alarm_img = QPixmap("warning.png")
        #set initial image as search image
        self.ui.label.setPixmap(self.ble_search)
        # initialize the clock worker
        self.clock = ClockWorker()
        self.clock.start()
        self.clock.signals.result.connect(self.showlcd)
        # connect the close button to exit command
        self.ui.pushButton.clicked.connect(self.exit)
        # initialize the bluetooth worker class
        self.bluetooth_worker = BluetoothWorker()
        self.bluetooth_worker.start()
        self.bluetooth_worker.signals.result.connect(self.alarm_check)
        # initialize the beeper
        self.beeper = BeepWorker()
        self.beeper.start()
        
    def alarm_check(self, sig):
        if sig:
            self.ui.label.setPixmap(self.alarm_img)
            self.beeper.turn_on()
        else:
            self.ui.label.setPixmap(self.ble_connect)
    
    
    def showlcd(self, sig):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.ui.lcdNumber.display(text)
        self.ui.lcdNumber.repaint()     
        
    '''this function exits the UI'''
    def exit(self,):
        self.clock.stop()
        sys.exit() 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())