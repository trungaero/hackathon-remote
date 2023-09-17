import serial
import serial.tools.list_ports
import time
import json
from typing import Dict

class Commands:
    SET_MODE  = 'm'
    SET_SPEED = 's'
    SET_FOOT  = 'f'
    SET_ARM   = 'a'
    SET_DISP  = 'd'
    MOVE      = 'n'
    HOLD      = ' '

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

# class ArmDirection:
#     NULL = 0
#     PULL = 1
#     PUSH = 2





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
        self.debug = False

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
        as_bytes = bytes(f'{cmd}{value}', encoding='utf-8') 
        if self.debug:
            print(as_bytes)
        else:
            self.ser.write(as_bytes)

    def recv(self):
        line = None
        try:
            line = self.ser.readline().decode('utf-8').strip()
        except:
            pass
        return line

    def recv_data(self):
        raw = self.recv()
        if raw:
            try:
                data = json.loads(raw.strip())
                if 'm' in data and data['m']==0  and len(data['p'])==12:
                    return CustomPacket(data['p'])
            except:
                pass

           
class Packet:
    def __init__(self, p_data: Dict):
        self.port_A = p_data[0]
        self.port_B = p_data[1]
        self.port_C = p_data[2]
        self.port_D = p_data[3]
        self.port_E = p_data[4]
        self.port_F = p_data[5]
        self.accel  = p_data[6]
        self.gyro   = p_data[7]
        self.attitude = p_data[8]
        self.unknown = p_data[9]
        self.time = p_data[10]
        self.reserve = p_data[11]


class MotorData:
    def __init__(self, p_data):
        self.speed = p_data[1][0]
        self.rel_pos = p_data[1][1]
        self.abs_pos = p_data[1][2]
        self.pwm = p_data[1][3]


class CustomPacket(Packet):
    def left_motor(self):
        return MotorData(self.port_B)
    
    def right_motor(self):
        return MotorData(self.port_A)
