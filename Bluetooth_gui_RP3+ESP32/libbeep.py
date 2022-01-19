import RPi.GPIO as GPIO
import time
from PyQt5.QtCore import QThread

def safe_sleep(asQthread:bool, seconds:float):
    """[summary]

    Args:
        asQthread (bool): specifiy whether the sleep function is for Qthread or native python
        seconds (float): seconds for sleep function
    """
    if asQthread:
        QThread.msleep(int(seconds*1000))
    else:
        time.sleep(seconds)

class Beeper:
    def __init__(self, buzzerpin = 7, asQthread= False):
        """Control class for buzzer on Rpi

        Args:
            buzzerpin (int, optional): Rpi pin where the buzzer is connected. Defaults to 7.
        """
        self.BuzzerPin = 7
        
        self.asQthread = asQthread
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.BuzzerPin, GPIO.OUT)
        self.off()
        

    def setup(self, pin:int):
        """setup the GPIO board, defaults buzzer to LOW/OFF
        """
        GPIO.setmode(GPIO.BOARD)
        # global BuzzerPin
        GPIO.setup(self.BuzzerPin, GPIO.OUT)
        GPIO.output(self.BuzzerPin, GPIO.LOW)


    def beep(self, seconds:float):    
        """Beep once for specified time in seconds

        Args:
            seconds (float): seconds the beep sound is produced.
        """
        print('BEEPING')
        GPIO.output(self.BuzzerPin,GPIO.HIGH)
        safe_sleep(self.asQthread, seconds)
        GPIO.output(self.BuzzerPin,GPIO.LOW)

    def beepAction(self, seconds:float, delay:float, repeat:float,):
        """specify a on--off on--off pattern for beep

        Args:
            seconds (float): seconds to beep
            delay (float): time to pause beep
            repeat (float): number of times to repeat the pattern
        """
        
        
        for _ in range(repeat):
            self.beep(seconds)
            safe_sleep(self.asQthread, delay)
            
    def beep_while(self, seconds:float, delay:float, repeat:float):
        # self.inAct = True
        self.action = True
        while self.action:
            self.beepAction(seconds, delay, repeat)  
            self.action = False     
            break 


    def off(self,):
        """switch off the beep
        """
        GPIO.output(self.BuzzerPin,GPIO.LOW)