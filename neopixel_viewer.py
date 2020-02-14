from emulator_backend import Adafruit_NeoPixel
from neopixel_effects import NeoPixel_Effects

def run():
    pixels = Adafruit_NeoPixel(51,6,"NEO_GRB + NEO_KHZ800")
    effects = NeoPixel_Effects(pixels)
    pixels.begin()
    pixels.setBrightness(100)
    pixels.setPixelColor(2,pixels.Color(255,200,10))
    pixels.show()
    pixels.delay(200)
    pixels.fill(pixels.Color(150,60,10),4,10)
    pixels.show()
    pixels.delay(1000)
    pixels.clear()
    effects.colorWipe(pixels.Color(200,12,70),50)
    pixels.setBrightness(70)
    pixels.clear()
    pixels.show()
    pixels.delay(1000)
    for i in range(5):
        effects.colorWipe(pixels.Color(200,0,200),10)
        pixels.clear()
    pixels.setBrightness(90)
    effects.rainbow(20)
    effects.colorWipe(pixels.Color(150,150,0),40)
    effects.rainbowCycle(20,2)

run()
