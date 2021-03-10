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
  
        # Converting the image to greyscale, as edge detection  
        # requires input image to be of mode = Greyscale (L) 
        image = image.convert("L") 
        
        # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES 
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE) 
        
        # Saving the Image Under the name Edge_Sample.png 
        return image

if __name__ == '__main__':
    Process('images/family.jpeg').edge()