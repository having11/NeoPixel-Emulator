class Pixel():
    def __init__(self, position):
        self.position = position
        self.current_color = (0,0,0)
    def update_color(self, new_color):
        self.current_color = new_color
    def get_position(self):
        return self.position
    def get_color(self):
        return self.current_color