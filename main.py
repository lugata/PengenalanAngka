# Pastikan untuk menginstall library yang dibutuhkan dengan menggunakan perintah pip
# seperti berikut:
# install up to python 3.7
# pip install opencv-python
# pip install tensorflow
# pip install numpy
# pip install keras

# oneline install with gpu : pip install opencv-python numpy tensorflow keras 
# oneline install cpu only : pip install opencv-python numpy tensorflow-cpu keras 

import cv2
import numpy as np
import tensorflow.keras as keras

# Load model yang telah dilatih sebelumnya
model = keras.models.load_model("model/model.h5") 

#url = "http://10.7.109.189:8080/video" #untuk menggunakan wireless eksternal camera
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW) #gunakan ini ketika menggunakan integrated camera "0 + cv2.CAP_DSHOW"
cv2.CAP_DSHOW
WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 

#function prediksi
def prediction(image, model):
    img = cv2.resize(image, (28, 28))
    img = img / 255
    img = img.reshape(1, 28, 28, 1)
    predict = model.predict(img)
    prob = np.amax(predict)
    class_index = np.argmax(predict,axis=1)
    result = class_index[0]

    if prob < 0.80:
        result = 0
        prob = 0
    return result, prob


while True:

    _, frame = cap.read()
    frame1 = frame.copy()

    bbox_size = (100, 100)
    bbox = [(int(WIDTH // 2 - bbox_size[0] // 2), int(HEIGHT // 2 - bbox_size[1] // 2)),
            (int(WIDTH // 2 + bbox_size[0] // 2), int(HEIGHT // 2 + bbox_size[1] // 2))]

    img_cropped = frame[bbox[0][1]:bbox[1][1], bbox[0][0]:bbox[1][0]]
    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.resize(img_gray, (200, 200))
    cv2.imshow("cropped", img_gray)

    result, probability = prediction(img_gray, model)
    cv2.putText(frame1, f"Prediction: {result}", (40, 50), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2,
                cv2.LINE_AA)
    cv2.putText(frame1, "Probability: " + "{:.2f}".format(probability), (40, 80), cv2.FONT_HERSHEY_DUPLEX, 0.8,
                (0, 255, 0), 2, cv2.LINE_AA)

    cv2.rectangle(frame1, bbox[0], bbox[1], (0, 255, 0), 3)

    cv2.imshow("input", frame1)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
