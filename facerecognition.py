''' Identifying a particular Person in a group of People'''

# Import necessary stuff
import os
import face_recognition
from PIL import Image

# Load the images
image1 = face_recognition.load_image_file('Gal1.jpg')
image2 = face_recognition.load_image_file('JL.jpg')

# Create encodings of the person to be identified in the group picture
original_image_encoded = face_recognition.face_encodings(image1)[0]

# Finding face locations in group picture
face_locations = face_recognition.face_locations(image2)

# Finding number of faces
print(len(face_locations))

# Iterating through face_location to seperate and display faces in image
for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image2[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    current_image_encoded = face_recognition.face_encodings(face_image)[0]
    result = face_recognition.compare_faces(
        [original_image_encoded], current_image_encoded)
    if(result[0]==True):
         pil_image.show()
         break
