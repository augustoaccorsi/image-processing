# https://realpython.com/face-recognition-with-python/
# https://realpython.com/traditional-face-detection-python/
# https://pypi.org/project/face-recognition/    
# https://betterprogramming.pub/step-by-step-face-recognition-in-images-ad0ad302058a

import cv2
import numpy as np
#import uuid, os, sys
from flask import jsonify

#from ...database import app
#from ...database import models

class Detection:
    def __init__(self, image):
        self.image = image
    '''
    def save(self, file):
        image_id = uuid.uuid4().hex
        try:
            filename = app.images.save(file, name=image_id+'.')
        except:
            return jsonify({'error': 'Could not store the image'}), 500

        _, image_ext = os.path.splitext(filename)

        # Add the metadata entry to the db
        image_metadata = models.ImageMetadata(id=image_id, file_ext=image_ext)
        app.db.session.add(image_metadata)
        app.db.session.commit()

        return jsonify({
            "image_id": image_id,
            "filename": filename
        }), 201
    '''
    def detect(self):
        # Read image from your local file system
        original_image = self.image

        # Convert color image to grayscale for Viola-Jones
        grayscale_image = cv2.cvtColor(np.asarray(self.image), cv2.COLOR_RGB2GRAY)

        # Load the classifier and create a cascade object for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        mouth_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

        detected_faces = face_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_faces:
            cv2.rectangle(
                grayscale_image,
                (column, row),
                (column + width, row + height),
                (255, 0, 0),
                2
            )
        ''' 
        detected_eyes = eye_cascade.detectMultiScale(grayscale_image)
        for (column, row, width, height) in detected_eyes:
            cv2.rectangle(
                original_image,
                (column, row),
                (column + width, row + height),
                (0, 255, 0),
                2
            )
   
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

        return grayscale_image

        #cv2.imwrite(self.image, original_image)

        #cv2.imshow('Image', original_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

