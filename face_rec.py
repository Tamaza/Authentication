# import the libraries
import os
import face_recognition


def analize():

    a = 0
    images = os.listdir('images')
    image_to_be_matched = face_recognition.load_image_file('camera.png')
    image_to_be_matched_encoded = face_recognition.face_encodings(
        image_to_be_matched)[0]


    for image in images:
        current_image = face_recognition.load_image_file("images/" + image)
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        result = face_recognition.compare_faces(
            [image_to_be_matched_encoded], current_image_encoded)
        if result[0] == True:
            print ("Matched: " + image)
            a+=1
            return 3

        else:
            print ("Not matched: " + image)
