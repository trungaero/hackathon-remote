import serial
import serial.tools.list_ports
import time

class Commands:
    SET_MODE  = 'm'
    SET_SPEED = 's'
    SET_FOOT  = 'f'
    SET_ARM   = 'a'
    SET_DISP  = 'd'
    MOVE      = 'n'

class Mode:
    MANUAL = 0
    AUTO1  = 1
    AUTO2  = 2
    AUTO3  = 3

class Direction:
    FORWARD  = 1
    BACKWARD = 2
    RLEFT    = 3
    RRIGHT   = 4

class ArmDirection:
    NULL = 0
    PULL = 1
    PUSH = 2





def list_ports():
    # Get a list of available serial ports
    ports = serial.tools.list_ports.comports()
    return [p.device for p in ports]


class ComPort:
    BAUD = 9600
    BYTESIZE = 8
    PARITY = 'N'
    STOPBITS = 1
    TIMEOUT = 0.1

    def __init__(self, device_name):
        self.device_name = device_name
        self.ser = None
        self.debug = True

    def is_available(self):
        return self.device_name in list_ports()

    def connect(self) -> bool:
        try:
            self.ser = serial.Serial(self.device_name, baudrate=self.BAUD, timeout=self.TIMEOUT)
            print(f'Connected!')
            return True
        except:
            print(f'Failed to connect to {self.device_name}')
        return False

    def close(self):
        if self.ser is not None:
            print(f'Disconnected!')
            self.ser.close()

    def send(self, cmd, value=''):       
        as_bytes = bytes(f'{cmd}{value}\n', encoding='utf-8') 
        if self.debug:
            print(as_bytes)
        self.ser.write(as_bytes)

    def recv(self):
        line = None
        try:
            # line = self.ser.read(10)
            line = self.ser.readline().decode('utf-8').strip()
            # print(len(line))
        except:
            pass
        return line



class Parser:
    pass



if __name__ == '__main__':
    c = ComPort('COM9')
    ser = c.connect()
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            print(line)
    with serial.Serial('COM9', 9600, timeout=0) as ser:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(line)