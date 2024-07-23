# Importando bibliotecas
import cv2
import numpy as np
from keras.models import load_model

# Instalando bibliotecas
# pip install tensorflow keras opencv-python

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Função de pré-precessamento

def preProcess(img):
    # Alterando a imagem para processar a imagem
    imgPre = cv2.GaussianBlur(img,(5,5),3)    
    imgPre = cv2.Canny(imgPre,90,140)
    kernel = np.ones((4,4),np.uint8)
    imgPre = cv2.dilate(imgPre,kernel,iterations=2)
    imgPre = cv2.erode(imgPre,kernel,iterations=2)
    return imgPre

# Repetição
while True:
    ret, img = video.read()
    if not ret:
        print("Erro ao capturar imagem")
        break

    # Imagem normal
    img = cv2.resize(img, (640, 480))
    
    # Imagem pré processada
    imgPre = preProcess(img)

    countors,hi = cv2.findContours(imgPre,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE )

    # Contador de objetos
    for contorno in countors:
        area = cv2.contourArea(contorno)

        # Reconhecendo o que são as moedas e o que não são
        if area > 2000:
            x,y,width,height = cv2.boundingRect(contorno)
            cv2.rectangle(img,(x,y),(x + width, y + height,),(0, 255, 0),2)

           
    cv2.imshow('IMG', img)
    cv2.imshow('IMG PRE-PROCESSADA', imgPre)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
