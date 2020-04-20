from pyfirmata import Arduino, util
import time
import Audio

class Button:
    lastClick = False
    butttype = False #False= pulldown, True = pullup
    pin = None
    def __init__(self, pin, butttype):
        self.pin = pin
        self.butttype = butttype
    def read(self):
        if (self.lastClick != True and self.pin.read() != self.butttype):
            self.lastClick = True
            return True
        elif(self.pin.read() == self.butttype):
            self.lastClick = False
        return False

board = Arduino('COM3')

iterator = util.Iterator(board)
iterator.start()

activeDio = 0
dios = []
for i in range(8,12):
    dios.append(board.get_pin('d:' + str(i) + ':o'))
buttUp = Button(board.get_pin('d:13:i'), False)
buttDn = Button(board.get_pin('d:12:i'), False)
buttGo = Button(board.get_pin('d:7:i'), False)

time.sleep(1.0)

while(True):
    if(buttUp.read() == True and activeDio < 3):
        dios[activeDio].write(False)
        activeDio += 1
    elif(buttDn.read() == True and activeDio > 0):
        dios[activeDio].write(False)
        activeDio -= 1
    if(buttGo.read() == True):
        Audio.playSans(activeDio)
        print("Done playing")
    dios[activeDio].write(True)

board.exit()