class Adafruit_GFX():
    def __init__(self):
        self.width = 0
        self.height = 0
        self.rotation = 0
        self.absoluteWidth = 0
        self.absoluteHeight = 0
    #must define this function in matrix subclass
    def drawPixel(self, x, y, color):
        pass
    def mapPixelToRotation(self, x, y):
        if (x < 0) or (y < 0) or (x >= self.width) or (y >= self.height):
            return None, None
        t = 0
        if self.rotation == 1:
            t = x
            x = self.absoluteWidth - 1 - y
            y = t
        elif self.rotation == 2:
            x = self.absoluteWidth - 1 - x
            y = self.absoluteHeight - 1 - y
        elif self.rotation == 3:
            t = x
            x = y
            y = self.absoluteHeight - 1 - t
        return x, y
    def setRotation(self, r):
        self.rotation = (r&3)
        if self.rotation == 0:
            pass
        elif self.rotation == 2:
            self.width = self.absoluteWidth
            self.height = self.absoluteHeight
        elif self.rotation == 1:
            pass
        elif self.rotation == 3:
            self.width = self.absoluteHeight
            self.height = self.absoluteWidth

    def invertDisplay(self, i):
        pass
    def drawFastVLine(self, x, y, h, color):
        self.drawLine(x, y, x, y+h-1, color)
    def drawFastHLine(self, x, y, w, color):
        self.drawLine(x, y, x+w-1, y, color)
    def drawLine(self, x0, y0, x1, y1, color):
        steep = abs(y1-y0) > abs(x1-x0)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = abs(y1 - y0)
        err = int(dx / 2)
        ystep = 0
        if y0 < y1:
            ystep = 1
        else:
            ystep = -1
        while x0 <= x1:
            if steep:
                self.drawPixel(y0, x0, color)
            else:
                self.drawPixel(x0, y0, color)
            err -= dy
            if err < 0:
                y0 += ystep
                err += dx
            x0 += 1
    def fillRect(self, x, y, w, h, color):
        for i in range(x, x+w):
            self.drawFastVLine(i, y, h, color)
    def fillScreen(self, color):
        self.fillRect(0,0,self.width,self.height, color)
    def clearScreen(self):
        self.fillScreen((0,0,0))
    def drawRect(self, x, y, w, h, color):
        self.drawFastHLine(x, y, w, color)
        self.drawFastHLine(x, y+h-1, w, color)
        self.drawFastVLine(x, y, h, color)
        self.drawFastVLine(x+w-1, y, h, color)
    def drawCircle(self, x0, y0, r, color):
        r = int(r)
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r
        x = 0
        y = r
        self.drawPixel(x0, y0+r, color)
        self.drawPixel(x0, y0-r, color)
        self.drawPixel(x0+r, y0, color)
        self.drawPixel(x0-r, y0, color)

        while x<y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x
            self.drawPixel(x0+x, y0+y, color)
            self.drawPixel(x0-x, y0+y, color)
            self.drawPixel(x0+x, y0-y, color)
            self.drawPixel(x0-x, y0-y, color)
            self.drawPixel(x0+y, y0+x, color)
            self.drawPixel(x0-y, y0+x, color)
            self.drawPixel(x0+y, y0-x, color)
            self.drawPixel(x0-y, y0-x, color)
    def drawCircleHelper(self, x0, y0, r, cornername, color):
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r
        x = 0
        y = r

        while x<y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x

            if cornername & 4:
                self.drawPixel(x0+x, y0+y, color)
                self.drawPixel(x0+y, y0+x, color)
            if cornername & 2:
                self.drawPixel(x0+x, y0-y, color)
                self.drawPixel(x0+y, y0-x, color)
            if cornername & 8:
                self.drawPixel(x0-y, y0+x, color)
                self.drawPixel(x0-x, y0+y, color)
            if cornername & 1:
                self.drawPixel(x0-y, y0-x, color)
                self.drawPixel(x0-x, y0-y, color)

    def fillCircle(self, x0, y0, r, color):
        self.drawFastVLine(x0, y0-r, 2*r+1, color)
        self.fillCircleHelper(x0, y0, r, 3, 0, color)
    def fillCircleHelper(self, x0, y0, r, corners, delta, color):
        f = 1 - r
        ddF_x = 1
        ddF_y = -2 * r
        x = 0
        y = r
        px = x
        py = y
        delta += 1

        while x < y:
            if f >= 0:
                y -= 1
                ddF_y += 2
                f += ddF_y
            x += 1
            ddF_x += 2
            f += ddF_x
            if x < (y+1):
                if corners & 1:
                    self.drawFastVLine(x0+x, y0-y, 2*y+delta, color)
                if corners & 2:
                    self.drawFastVLine(x0-x, y0-y, 2*y+delta, color)
            if y != py:
                if corners & 1:
                    self.drawFastVLine(x0+py, y0-px, 2*px+delta, color)
                if corners & 2:
                    self.drawFastVLine(x0-py, y0-px, 2*px+delta, color)
                py = y
            px = x
    def drawTriangle(self, x0, y0, x1, y1, x2, y2, color):
        self.drawLine(x0,y0,x1,y1,color)
        self.drawLine(x1,y1,x2,y2,color)
        self.drawLine(x2,y2,x0,y0,color)
    def fillTriangle(self, x0, y0, x1, y1, x2, y2, color):
        a, b, y, last = 0, 0, 0, 0
        if y0 > y1:
            y0, y1 = y1, y0
            x0, x1 = x1, x0
        if y1 > y2:
            y2, y1 = y1, y2
            x2, x1 = x1, x2
        if y0 > y1:
            y0, y1 = y1, y0
            x0, x1 = x1, x0
        if y0 == y2:
            a = b = x0
            if x1 < a:
                a = x1
            elif x1 > b:
                b = x1
            if x2 < a:
                a = x2
            elif x2 > b:
                b = x2
            self.drawFastHLine(a, y0, b-a+1, color)
            return True
        dx01 = x1 - x0
        dy01 = y1 - y0
        dx02 = x2 - x0
        dy02 = y2 - y0
        dx12 = x2 - x1
        dy12 = y2 - y1
        sa = 0
        sb = 0 
        if y1==y2:
            last = y1
        else:
            last = y1-1
        for y in range(y0,last+1):
            a = int(x0+sa/dy01)
            b = int(x0+sb/dy02)
            sa += dx01
            sb += dx02
            if a > b:
                a, b = b, a
            self.drawFastHLine(a,y,b-a+1,color)
        sa = dx12 * (y-y1)
        sb = dx02 * (y-y0)
        while(y<=y2):
            a = int(x1 + sa / dy12)
            b = int(x0 + sb / dy02)
            sa += dx12
            sb += dx02
            if a > b:
                a, b = b, a
            self.drawFastHLine(a, y, b-a+1, color)
            y += 1
    def drawRoundRect(self, x, y, w, h, radius, color):
        r = radius
        max_radius = 0
        if w < h:
            max_radius = w
        else:
            max_radius = h
        max_radius = int(max_radius/2)
        if r > max_radius:
            r = max_radius
        self.drawFastHLine(x+r,y,w-2*r,color)
        self.drawFastHLine(x+r,y+h-1,w-2*r,color)
        self.drawFastVLine(x,y+r,h-2*r,color)
        self.drawFastVLine(x+w-1,y+r,h-2*r,color)

        self.drawCircleHelper(x+r,y+r,r,1,color)
        self.drawCircleHelper(x+w-r-1, y+r, r, 2, color)
        self.drawCircleHelper(x+w-r-1,y+h-r-1, r, 4, color)
        self.drawCircleHelper(x+r, y+h-r-1, r, 8, color)

    def fillRoundRect(self, x, y, w, h, radius, color):
        r = radius
        max_radius = 0
        if w < h:
            max_radius = w
        else:
            max_radius = h
        max_radius = int(max_radius/2)
        if r > max_radius:
            r = max_radius
        self.fillRect(x+r,y,w-2*r,h,color)
        self.fillCircleHelper(x+w-r-1, y+r, r, 1, h-2*r-1, color)
        self.fillCircleHelper(x+r, y+r, r, 2, h-2*r-1, color)
    def drawBitmap(self, x, y, bitmap_array, w, h, color, background_color=(0,0,0)):
        self.fillRect(x,y,w,h,background_color)
        byteWidth = int((w+7)/8)
        byte = 0
        for j in range(h):
            for i in range(w):
                if i & 7:
                    byte <<= 1
                else:
                    byte = bitmap_array[int(j*byteWidth+i/8)]
                if byte & 0x80:
                    self.drawPixel(x+i, y, color)
            y += 1
    def getRotation(self):
        return self.rotation