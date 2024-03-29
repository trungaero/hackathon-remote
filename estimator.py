import math
from communication import ComPort, CustomPacket
import json

# CHASIS CONSTANTS
R_WHEEL = 5.6 / 2 / 100
L_CHASSIS = 0.095

# MATH CONSTANTS  
RAD2DEG = 180 / math.pi
DEG2RAD = 1 / RAD2DEG

class Navigator:
    def __init__(self, x0=0, y0=0, the0=0):
        self.last_packet = None
        self.x = x0
        self.y = y0
        self.the = the0

    def reset(self, x=0, y=0, the=0):
        self.x = x
        self.y = y
        self.the = the

    def __calc_dwheel(self, phi0, phi1, speed, sign=1):
        """
            phi0: last position in degree (0 - 360)
            phi1: cur position in degree (0 - 360)
            speed: speed in deg/s 

            return: change in angle
        """
        dphi = phi1 - phi0
        return sign * dphi

        # if speed > 0:
        #     if dphi >= 0:
        #         return dphi
        #     else:
        #         return dphi + 360
        # elif speed < 0:
        #     if dphi < 0:
        #         return dphi
        #     else:
        #         return dphi - 360
        # else:
        #     return 0

    def update(self, packet: CustomPacket):
        """
            dr: change in right wheel angle
            dl: change in left wheel angle
        """
        if self.last_packet is not None:
            # dl = self.__calc_dwheel(self.last_packet.left_motor().rel_pos,
            #                         packet.left_motor().rel_pos,
            #                         packet.left_motor().speed)
            dl = self.__calc_dwheel(self.last_packet.left_motor().rel_pos,
                                    packet.left_motor().rel_pos,
                                    packet.left_motor().speed, -1)

            dr = self.__calc_dwheel(self.last_packet.right_motor().rel_pos,
                                    packet.right_motor().rel_pos,
                                    packet.right_motor().speed)


            dthe = R_WHEEL / L_CHASSIS * (dl - dr)
            
            self.the += dthe

            if self.the > 180:
                self.the -= 360
            if self.the < -180:
                self.the += 360

            dx = (R_WHEEL/2) * math.sin(self.the * DEG2RAD) * (dr + dl) * DEG2RAD
            dy = (R_WHEEL/2) * math.cos(self.the * DEG2RAD) * (dr + dl) * DEG2RAD

            self.x += dx * 100
            self.y += dy * 100

            self.last_packet = packet

            # print((self.x, self.y, self.the, dl, dr, self.last_packet.left_motor().rel_pos, packet.left_motor().rel_pos, self.last_packet.right_motor().rel_pos, packet.right_motor().rel_pos))

        else:
            self.last_packet = packet
