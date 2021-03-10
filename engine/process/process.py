# https://realpython.com/face-recognition-with-python/
# https://realpython.com/traditional-face-detection-python/

import numpy as np
from PIL import Image, ImageFilter 

class Process:

    def edge(self, image):
        image = Image.open(image) 
        image = image.convert("L") 
        image = image.filter(ImageFilter.FIND_EDGES) 
        
        return image

    def mandelbrot(self, width, height, max_iter):
        # Default size is 500x500 - note this takes around 90 seconds on a Raspberry Pi
        if width != None:
            WIDTH = width
        else:
            WIDTH = 500
        if height != None:
            HEIGHT = height
        else:
            HEIGHT = 500
        if max_iter != None:
            MAX_ITER = max_iter
        else:
            MAX_ITER = 500

        pix = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

        # For each pixel in our little display...
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):
                zoom = 0.3
                
            # The z in the mandelbrot set is an imaginary number, made up of
            # a real number and an imaginary number. These two variables are
            # how I represent that
                real = (float(x) / float(WIDTH)) * (1.0 / zoom) + -2.1 
                imaginary = (float(y) / float(HEIGHT)) * (1.0 / zoom) + -1.6
                
            # This is the constant, which is the 'c' element of the main equation (z=z2+c)	
                const_real = real
                const_imaginary = imaginary

                # Used to hold the (z2 element, believe it or not)
                z2 = 0.0

                iter_count = 0

                for iter_loop in range(0, MAX_ITER):
                    temp_real = real

                # Calculate z=z2+c
                    real = (temp_real * temp_real) - (imaginary * imaginary) + const_real
                    imaginary = 2.0 * temp_real * imaginary + const_imaginary
                    z2 = real * real + imaginary * imaginary

                    iter_count = iter_loop

                # If z2 exceeds 4.0 before we hit MAX_ITER then we exit the loop and the current pixel
                # does not belong to the mandelbrot 
                    if z2 > 4.0:
                        break

                # Plot the current pixel. If it's in the mandelbrot set then do nothing because it's already black
                if z2 > 4.0:            
                    c = iter_count * 10 % 255
                    if c > 50:
                        pix.itemset((y,x, 2), c)
                    else:
                        pix.itemset((y,x,2), 50)
            
        # Done. Save and quit
        mandelbrot = Image.fromarray(pix, 'RGB')
        return mandelbrot

if __name__ == '__main__':
    Process().mandelbrot()