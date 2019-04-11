from emulator_backend import Adafruit_NeoPixel
from neopixel_effects import NeoPixel_Effects

def run():
    pixels = Adafruit_NeoPixel(50,6,"NEO_GRB + NEO_KHZ800")
    effects = NeoPixel_Effects(pixels)
    pixels.gui.render()
    event = pixels.gui.dispatch_events()
    pixels.begin()
    pixels.setBrightness(80)
    pixels.setPixelColor(2,pixels.Color(160,200,10))
    pixels.show()
    pixels.delay(1000)
    pixels.fill(pixels.Color(150,60,10),4,40)
    pixels.show()
    pixels.delay(1000)
    pixels.setBrightness(40)
    pixels.clear()
    pixels.show()
    pixels.delay(1000)
    for i in range(2):
        for j in range(pixels.numPixels()):
            pixels.setPixelColor(j,pixels.Color(200,10,200))
            pixels.show()
        pixels.clear()
    pixels.setBrightness(90)
    effects.rainbow(20)
    effects.colorWipe(pixels.Color(150,150,0),40)
    effects.rainbowCycle(20,5)

run()
