import time
import board
import neopixel



class neopixel_class():

    def __init__(self) -> None:
        self.pixel_pin = board.D12
        self.num_pixels = 12
        self.ORDER = neopixel.GRB
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER)

    def wheel(self,pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


    def rainbow_cycle(self):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(0.001)


    def all_green(self):
        for i in range(self.num_pixels):
            self.pixels[i] = (0, 255, 0)
        self.pixels.show()
        
    #make 1/4 of the pixels green rest in red
    def green_red_1_4(self):
        self.pixels[0] = (0, 255, 0)
        self.pixels[1] = (0, 255, 0)
        self.pixels[2] = (0, 255, 0)
        self.pixels[3] = (255, 0, 0)
        self.pixels[4] = (255, 0, 0)
        self.pixels[5] = (255, 0, 0)
        self.pixels[6] = (255, 0, 0)
        self.pixels[7] = (255, 0, 0)
        self.pixels[8] = (255, 0, 0)
        self.pixels[9] = (255, 0, 0)
        self.pixels[10] = (255, 0, 0)
        self.pixels[11] = (255, 0, 0)
        self.pixels.show()
        
    def green_red_2_4(self):
        self.pixels[0] = (0, 255, 0)
        self.pixels[1] = (0, 255, 0)
        self.pixels[2] = (0, 255, 0)
        self.pixels[3] = (0, 255, 0)
        self.pixels[4] = (0, 255, 0)
        self.pixels[5] = (0, 255, 0)
        self.pixels[6] = (255, 0, 0)
        self.pixels[7] = (255, 0, 0)
        self.pixels[8] = (255, 0, 0)
        self.pixels[9] = (255, 0, 0)
        self.pixels[10] = (255, 0, 0)
        self.pixels[11] = (255, 0, 0)
        self.pixels.show()
        
    def green_red_3_4(self):
        self.pixels[0] = (0, 255, 0)
        self.pixels[1] = (0, 255, 0)
        self.pixels[2] = (0, 255, 0)
        self.pixels[3] = (0, 255, 0)
        self.pixels[4] = (0, 255, 0)
        self.pixels[5] = (0, 255, 0)
        self.pixels[6] = (0,255, 0)
        self.pixels[7] = (0,255, 0)
        self.pixels[8] = (0,255, 0)
        self.pixels[9] = (255, 0, 0)
        self.pixels[10] = (255, 0, 0)
        self.pixels[11] = (255, 0, 0)
        self.pixels.show()
    
    # def all_orange(self):
    #     for i in range(self.num_pixels):
    #         self.pixels[i] = (255, 165, 0)
    #     self.pixels.show()
        
    def all_red(self):
        for i in range(self.num_pixels):
            self.pixels[i] = (255, 0, 0)
        self.pixels.show()

