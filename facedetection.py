import cv2
import numpy as np
image = cv2.imread("images/face.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
#The face detection part
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100)
)

for (x, y, w, h) in faces:
    face_roi = image[y:y+h, x:x+w].copy()
    flipped_face = np.zeros_like(face_roi)
    for row in range(h):#vertical flip
        flipped_face[row, :] = face_roi[h - row - 1, :]
    image[y:y+h, x:x+w] = flipped_face
cv2.imwrite("flipped_face_vertical.jpg", image)
cv2.imshow("Vertically Flipped Face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
