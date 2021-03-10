# https://realpython.com/face-recognition-with-python/
# https://realpython.com/traditional-face-detection-python/

import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter 

class Process:
    def __init__(self, image):
        self.image = image

    def face(self):
        # Read image from your local file system

        #file_bytes = np.asarray(bytearray(self.image), dtype=np.uint8)
        #img = cv.imdecode(file_bytes, cv.IMREAD_COLOR)

        original_image = cv.imdecode(np.frombuffer(self.image, np.uint8), -1)
        
        #original_image = cv.imread(self.image)

        #print(original_image)
    
        # Convert color image to grayscale for Viola-Jones
        grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

        #print(grayscale_image)
        
        # Load the classifier and create a cascade object for face detection
        face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')
        eye_cascade = cv.CascadeClassifier('cascades/haarcascade_eye.xml')
        mouth_cascade = cv.CascadeClassifier('haarcascades/haarcascade_smile.xml')

        #print(face_cascade)
    
        detected_faces = face_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_faces:
            cv.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (255, 0, 0),
                2
            )

        detected_eyes = eye_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_eyes:
            cv.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (0, 255, 0),
                2
            )
        '''
        detected_mouth = mouth_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_mouth:
            cv.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (0, 0, 255),
                2
            )
        '''
        cv.imshow('Image', original_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def edge(self):
        image = Image.open(self.image) 
        image = image.convert("L") 
        image = image.filter(ImageFilter.FIND_EDGES) 
        
        return image

    def mandelbrot(self):
        # Default size is 500x500 - note this takes around 90 seconds on a Raspberry Pi
        WIDTH = 500
        HEIGHT = 500
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
    Process('images/family.jpeg').mandelbrot()