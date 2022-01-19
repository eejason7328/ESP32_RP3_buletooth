import bluetooth
import socket
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



class BLE:
    def __init__(self, asQthread = False):
        try:
            self.nearby_devices = bluetooth.discover_devices(lookup_names=True)
            print("Found {} devices.".format(len(self.nearby_devices)))
            self.names, self.address = [], []
            for addr, name in self.nearby_devices:
                print("  {} - {}".format(addr, name))
                self.names.append(name)
                self.address.append(addr)
        except:
            print("Cannot start Bluetooth!!!")
        
        self.asQthread = asQthread
        
            
    def select_device(self, MAC_ADD: str):
        
        serverMACAddress = 'B4:E6:2D:B3:0B:1B'   # e.g. '00:1f:e1:dd:08:3d'
        port = 1
        self.ble_device = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.connection = False
        try:
            self.ble_device.connect((serverMACAddress,port))
            print("Connected Successfully to device {}".format('B4:E6:2D:B3:0B:1B'))
            self.connection = True
        except:
            print("Could Not Connect to device: {}".format('B4:E6:2D:B3:0B:1B'))
            self.connection = False
        return self.connection
    
    def read(self, buffer_size = 8):
        msg = None
        try:
            msg = self.ble_device.recv(buffer_size)
        except:
            print("No message")
        return msg 
    
    def continous_read(self, buffer_size = 8, delay = 0.1):
        while self.connection:
            msg = None
            try:
                msg = self.ble_device(buffer_size).decode('utf-8')
            except:
                print("No message")
            safe_sleep(self.asQthread, delay)
            yield msg
            
    def stop(self,):
        self.connection = False
        self.ble_device.close()

#a = BLE()
