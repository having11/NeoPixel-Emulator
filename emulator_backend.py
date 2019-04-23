from pixel import Pixel
import time
from neopixel_emulator import NeoPixel_Emulator

class Adafruit_NeoPixel():
    def __init__(self, pixel_num, pixel_pin, pixel_type):
        self.pixel_number = pixel_num
        self.pin = pixel_pin
        self.pixel_type = pixel_type
        self.brightness = 100
    def begin(self, draw_matrix=False, width=0, height=0, window_w=1765, window_h=400):
        self.gui = NeoPixel_Emulator(window_w=window_w, window_h=window_h)
        self.pixel_list = list()
        for pixel in range(self.pixel_number):
            self.pixel_list.append(Pixel(pixel))
        if draw_matrix:
            self.gui.draw_LED_matrix(width, height)
        else:
            self.gui.draw_LEDs(self.pixel_number)
        self.gui.render()
    def show(self):
        #for pixel in self.pixel_list:
            #print("Pixel {0} has color {1}".format(pixel.get_position(),pixel.get_color()))
        self.gui.render()
    def setPixelColor(self, pixel_position, color):
        if pixel_position > self.pixel_number:
            return False
        self.gui.draw_color(pixel_position,color)
        self.pixel_list[pixel_position].update_color(color)
    def Color(self, r, g, b):
        return (r, g, b)
    def fill(self, color, start, count):
        if start > self.pixel_number:
            return False
        if start + count > self.pixel_number:
            return False
        else:
            for pixel in range(start,count+start):
                self.setPixelColor(pixel,color)
    def setBrightness(self, new_brightness): #use opacity to represent this
        if new_brightness >= 0 and new_brightness <= 100:
            self.brightness = new_brightness
            self.gui.change_brightness(self.brightness)
        else:
            return False
    def clear(self):
        self.fill((0,0,0),0,self.pixel_number)
    def numPixels(self):
        return self.pixel_number
    def getPixelColor(self,pixel_position):
        return self.pixel_list[pixel_position].get_color()
    def getPin(self):
        return self.pin
    def getBrightness(self):
        return self.brightness
    def delay(self, ms):
        time.sleep(ms/1000)
        