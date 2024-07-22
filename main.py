# Importando bibliotecas
import cv2
import numpy as np
from keras.models import load_model

# Instalando bibliotecas
# pip install tensorflow keras opencv-python

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, img = video.read()
    if not ret:
        print("Erro ao capturar imagem")
        break

    img = cv2.resize(img, (640, 480))

    cv2.imshow('IMG', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
