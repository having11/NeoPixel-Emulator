import pyglet
import math

class NeoPixel_Emulator(pyglet.window.Window):
    def __init__(self, window_w=1765, window_h=400):
        super(NeoPixel_Emulator,self).__init__(width=window_w, height=window_h)
        self.batch = pyglet.graphics.Batch()
        self.sprites = []
        self.color_sprites = []
        self.led_group = pyglet.graphics.OrderedGroup(0)
        self.color_group = pyglet.graphics.OrderedGroup(1)
        self.alive = 1
    def draw_LEDs(self, led_number):
        for led in range(led_number):
            img = pyglet.image.load('ws2812b.png')
            self.sprites.append(pyglet.sprite.Sprite(img=img,batch=self.batch, x=(led-50*(led//50))*35, y=self.height-34-((led//50)*34), group=self.led_group))
            self.color_sprites.append(pyglet.sprite.Sprite(img=pyglet.image.load('circle.png'),batch=self.batch,x=(led-50*(led//50))*35,y=self.height-34-((led//50)*34)-5,group=self.color_group))
            self.sprites[led].scale = .1
            self.color_sprites[led].color = (0,0,0)
            #print(self.sprites[led].position)
    def draw_LED_matrix(self, width, height):
        for y in range(height):
            for x in range(width):
                img = pyglet.image.load('ws2812b.png')
                self.sprites.append(pyglet.sprite.Sprite(img=img,batch=self.batch, x=x*35, y=self.height-34-(y*34), group=self.led_group))
                self.color_sprites.append(pyglet.sprite.Sprite(img=pyglet.image.load('circle.png'),batch=self.batch,x=x*35,y=self.height-34-(y*34)-5,group=self.color_group))
                self.sprites[y*width+x].scale = .1
                self.color_sprites[y*width+x].color = (0,0,0)
    def map(self,input_val,in_min,in_max,out_min,out_max):
        output=(input_val-in_min)/(in_max-in_min)*(out_max-out_min)+out_min
        return output
    def draw_color(self, led_position, color):
        self.color_sprites[led_position].color = color
    def draw_matrix_color(self, x, y, color, width):
        self.color_sprites[y*width+x].color = color
    def change_brightness(self,brightness):
        for sprite in self.color_sprites:
            sprite.opacity = self.map(brightness,0,100,0,255)
    def on_draw(self):
        self.render()
    def render(self):
        self.clear()
        self.batch.draw()
        event = self.dispatch_events()
        self.flip()