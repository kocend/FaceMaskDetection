import cv2
import keras
import numpy as np

imagenet = keras.models.load_model("imagenet.h5")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img_path = "tests/out.jpg"
im = cv2.imread(img_path)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# iterate over each face on the image
for (x, y, w, h) in faces:
    face_img = im[y:y + h, x:x + w]
    rerect_sized = cv2.resize(face_img, (224, 224))
    normalized = rerect_sized / 255.0
    reshaped = np.reshape(normalized, (1, 224, 224, 3))
    reshaped = np.vstack([reshaped])
    result = imagenet.predict(reshaped)
    print(result)

    if result[0][0] > 0.5:
        cv2.putText(im, "No mask", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 0, 255), 2)
    if result[0][0] <= 0.5:
        cv2.putText(im, "Mask" + str(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 2)

#write classified image to file
cv2.imwrite(img_path.replace(".", "_classified."), im)
