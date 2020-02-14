from emulator_backend import Adafruit_NeoPixel
from neopixel_gfx import Adafruit_GFX
from time import sleep

class Adafruit_NeoMatrix(Adafruit_GFX):
    positions = {"NEO_MATRIX_TOP":0,"NEO_MATRIX_BOTTOM":1,"NEO_MATRIX_LEFT":0,"NEO_MATRIX_RIGHT":2,\
        "NEO_MATRIX_CORNER":3,"NEO_MATRIX_ROWS":0,"NEO_MATRIX_COLUMNS":4,"NEO_MATRIX_AXIS":4,\
        "NEO_MATRIX_PROGRESSIVE":0,"NEO_MATRIX_ZIGZAG":8,"NEO_MATRIX_SEQUENCE":8}
    def create_matrix(self, width, height, pin, matrix_type):
        self.width = width
        self.height = height
        self.absoluteWidth = width
        self.absoluteHeight = height
        self.pin = pin
        self.matrix_type = matrix_type
        self.pixels = Adafruit_NeoPixel(self.width*self.height,self.pin,"NEO_GRB + NEO_KHZ800")
    def delay(self, ms):
        sleep(ms/1000)
    def begin(self):
        needed_w = self.width*35
        needed_h = self.height*34+4
        self.pixels.begin(draw_matrix=True,width=self.width,height=self.height, window_w=needed_w, window_h=needed_h)
    def drawPixel(self, x, y, color):
        x, y = self.mapPixelToRotation(x, y)
        if x == None or y == None:
            pass
        else:
            self.pixels.setPixelColor(y*self.width+x,color)
    def show(self):
        self.pixels.gui.render()
        event = self.pixels.gui.dispatch_events()
    def setBrightness(self, new_brightness): #use opacity to represent this
        if new_brightness >= 0 and new_brightness <= 100:
            self.brightness = new_brightness
            self.pixels.gui.change_brightness(self.brightness)
        else:
            return False

bitmap_array = [0x00, 0x84>>1, 0x84>>1, 0x00, 0x00, 0x84>>1, 0x78>>1, 0x00]

if __name__ == "__main__":
    matrix = Adafruit_NeoMatrix()
    matrix.create_matrix(15,10,6,matrix.positions["NEO_MATRIX_TOP"]+matrix.positions["NEO_MATRIX_LEFT"]+\
        matrix.positions["NEO_MATRIX_COLUMNS"]+matrix.positions["NEO_MATRIX_PROGRESSIVE"])
    matrix.begin()
    matrix.show()
    matrix.setRotation(0)
    matrix.setBrightness(90)
    matrix.drawPixel(0,0,(200,12,70))
    matrix.show()
    matrix.delay(2000)
    matrix.drawPixel(3,2,(200,12,70))
    matrix.show()
    matrix.delay(2000)
    matrix.fillRect(0,0,4,2,(200,12,70))
    matrix.show()
    matrix.delay(2000)
    matrix.fillScreen((200,12,70))
    matrix.show()
    matrix.delay(2000)
    matrix.fillCircle(5,5,3,(0,0,255))
    matrix.show()
    matrix.delay(2000)
    matrix.drawCircle(10,10,8,(0,255,0))
    matrix.show()
    matrix.delay(2000)
    matrix.fillRoundRect(0,0,10,6,3,(0,50,150))
    matrix.show()
    matrix.delay(2000)
    matrix.drawTriangle(0,0,9,2,4,9,(160,160,0))
    matrix.show()
    matrix.delay(2000)
    #matrix.clearScreen()
    matrix.drawBitmap(0,0,bitmap_array,8,8,(0,0,0),background_color=(200,200,200))
    matrix.show()
    matrix.delay(3000)
