# reference: https://stackoverflow.com/questions/23729886/udp-sockets-in-d-programming-language

import sys, socket, math, time
from ctypes import *

class Artnet:
    class ArtNetDMXOut(LittleEndianStructure):
        PORT = 0x1936
        _fields_ = [("id", c_char * 8),
                    ("opcode", c_ushort),
                    ("protverh", c_ubyte),
                    ("protver", c_ubyte),
                    ("sequence", c_ubyte),
                    ("physical", c_ubyte),         
                    ("universe", c_ushort),
                    ("lengthhi", c_ubyte),
                    ("length", c_ubyte),
                    ("payload", c_ubyte * 512)]
        
        def __init__(self):
            self.id = b"Art-Net"
            self.opcode = 0x5000
            self.protver = 14
            self.universe = 0
            self.lengthhi = 2

    def __init__(self):
        self.artnet = Artnet.ArtNetDMXOut()
        self.S = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    
        for i in range(512):
            self.artnet.payload[i] = 0

    def sendDMX(self,data,IP,port):
        # sendDMX(送るデータ,IPアドレス,ポート番号)
        self.artnet.universe = port
        for i in range(512):
            if(i < len(data)):
                self.artnet.payload[i] = data[i]
            else:
                break
        self.S.sendto(self.artnet,(IP,Artnet.ArtNetDMXOut.PORT))

if __name__ == '__main__':
    artnet = Artnet()
    data = [0] * 512
    for i in range(150):
        data[i*3+0] = 0
        data[i*3+1] = 0
        data[i*3+2] = 0
    artnet.sendDMX(data,"133.15.42.111",5)

