import math
from communication import ComPort, CustomPacket
import json

# CHASIS CONSTANTS
R_WHEEL = 0.05
L_CHASSIS = 0.14

# MATH CONSTANTS  
RAD2DEG = 180 / math.pi
DEG2RAD = 1 / RAD2DEG

class Navigator:
    def __init__(self, x0=0, y0=0, the0=0):
        self.last_packet = None
        self.x = x0
        self.y = y0
        self.the = the0

    def reset(self):
        self.x = 0
        self.y = 0
        self.the = 0

    def __calc_dwheel(self, phi0, phi1, speed):
        """
            phi0: last position in degree (0 - 360)
            phi1: cur position in degree (0 - 360)
            speed: speed in deg/s 

            return: change in angle
        """
        dphi = phi1 - phi0

        if speed > 0:
            if dphi >= 0:
                return dphi
            else:
                return dphi + 360
        elif speed < 0:
            if dphi < 0:
                return dphi
            else:
                return dphi - 360
        else:
            return 0

    def update(self, packet: CustomPacket):
        """
            dr: change in right wheel angle
            dl: change in left wheel angle
        """
        if self.last_packet is not None:
            dl = self.__calc_dwheel(self.last_packet.left_motor().rel_pos,
                                    packet.left_motor().rel_pos,
                                    packet.left_motor().speed)
            dr = self.__calc_dwheel(self.last_packet.right_motor().rel_pos,
                                    packet.right_motor().rel_pos,
                                    packet.right_motor().speed)


            dthe = R_WHEEL / L_CHASSIS * (dl - dr)
            
            self.the += dthe

            if self.the > 180:
                self.the -= 360
            if self.the < -180:
                self.the += 360

            dx = (R_WHEEL/2) * math.sin(self.the * DEG2RAD) * (dr + dl)
            dy = (R_WHEEL/2) * math.cos(self.the * DEG2RAD) * (dr + dl)

            self.x += dx
            self.y += dy

            self.last_packet = packet

            print((self.x, self.y, self.the, dl, dr, self.last_packet.left_motor().rel_pos, packet.left_motor().rel_pos, self.last_packet.right_motor().rel_pos, packet.right_motor().rel_pos))

        else:
            self.last_packet = packet
