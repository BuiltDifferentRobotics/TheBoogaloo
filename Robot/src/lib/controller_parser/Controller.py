from digi.xbee.devices import XBeeDevice


class Controller:

    def __init__(self, xbee):
        if(xbee):
            self.device = XBeeDevice("COM1", 9600)
            self.device.open()
        self.inputs = [None] * 17

    def readData(self):
        ip_message = self.device.read_data()
        self.decodeMsg(ip_message)
        
    def decodeMsg(self, message):
        #HX:  0 HY:  0 A0:-1471 A1: 52 A2:-52 A3:3178 Y:0 B:0 A:0 X:0 THL:0 THR:0 TL:0 TR:0 TL2:0 TR3:0 M:0 ST:0 N:0 E:0 S:0 W:0 SL:0 EN: 0 AE: 0
        messages = message.split()
        for i in range(17):
            self.inputs[i] = float(messages[2*i+1].strip(""))

def main():
    c = Controller(False)
    c.decodeMsg("HX:   0  HY:   0  A0: 2205  A1: -671  A2: -4475  A3: 4493  Y: 0  B: 0  A: 0  X: 0  THL: 0  THR: 0  TL: 0  TR: 0  TL2: 0  TR3: 0  M: 0  ST: 0  N: 0  E: 0  S: 0  W: 0  SL: 0 EN: 0 AE: 0")
    print(*c.inputs)

if __name__ == "__main__":
    main()

