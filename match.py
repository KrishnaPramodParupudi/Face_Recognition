''' Finding whether people in two images are the same '''


# import necessary stuff
import face_recognition

# load images first one is used to train and second one to verify the person
image1 = face_recognition.load_image_file('Gal1.jpg')
image2 = face_recognition.load_image_file('Gal2.jpg')

# face_encodings gives a list of encodings of all faces in an image and here, since we have only one face, we took only the zeroth index
original_image_encoded = face_recognition.face_encodings(image1)[0]
current_image_encoded = face_recognition.face_encodings(image2)[0]

# Comparision of face in current image with a list of encoded images
result = face_recognition.compare_faces(
        [original_image_encoded], current_image_encoded)

# compare_faces gives a list of boolean values, if there is match, it's true else false
if(result[0]==True):
    print("There is a match")
else:
    print("There is no match")

