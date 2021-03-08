# https://realpython.com/face-recognition-with-python/
# https://realpython.com/traditional-face-detection-python/

import cv2 as cv

class Detection:
    def __init__(self, image):
        self.image = image

    

    def detect(self):
        # Read image from your local file system
        original_image = cv.imread(self.image)

        # Convert color image to grayscale for Viola-Jones
        grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

        # Load the classifier and create a cascade object for face detection
        face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_alt.xml')
        eye_cascade = cv.CascadeClassifier('cascades/haarcascade_eye.xml')
        mouth_cascade = cv.CascadeClassifier('haarcascades/haarcascade_smile.xml')


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

if __name__ == '__main__':
    Detection('images/family.jpeg').detect()
