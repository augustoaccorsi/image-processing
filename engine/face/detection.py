# https://realpython.com/face-recognition-with-python/
# https://realpython.com/traditional-face-detection-python/
# https://pypi.org/project/face-recognition/    
# https://betterprogramming.pub/step-by-step-face-recognition-in-images-ad0ad302058a

import cv2
import numpy as np
#import urllib.request

class Detection:
    def __init__(self, image):
        self.image = image

    def url_to_image(self, url):
        # download the image, convert it to a NumPy array, and then read
        # it into OpenCV format
        #resp = urllib.request.urlopen(url)
        #image = np.asarray(bytearray(resp.read()), dtype="uint8")
        #image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
        return np.array(url) 

        # return the image
        #return image

    def detect(self):
        # Read image from your local file system
        original_image = self.image

        # Convert color image to grayscale for Viola-Jones
        grayscale_image = cv2.cvtColor(np.asarray(self.image), cv2.COLOR_RGB2GRAY)

        # Load the classifier and create a cascade object for face detection
        face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')
        eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
        mouth_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')


        detected_faces = face_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_faces:
            cv2.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (255, 0, 0),
                2
            )
 
        detected_eyes = eye_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_eyes:
            cv2.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (0, 255, 0),
                2
            )
        '''
        detected_mouth = mouth_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_mouth:
            cv2.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (0, 0, 255),
                2
            )
        '''

        #cv2.imwrite(self.image, original_image)

        cv2.imshow('Image', original_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

