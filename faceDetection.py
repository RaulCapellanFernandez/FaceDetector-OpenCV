#Face Detection

#Librerias de OpenCV
import cv2

#Carga los filtros creados en el XML
cara_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ojo_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Deteccion
def detect(gray, imagen):
    #La imagen original y la imagen en blanco y negro
    #1.3 factor de reduccion de la imagen
    #5 zonas deben ser aceptadas
    faces = cara_cascade.detectMultiScale(gray, 1.3, 5)
    #Coordenadas desde arriba a la izquierda x,y
    #W ancho del rectangulo
    #H altura del rectangulo
    for(x,y,w,h) in faces: 
        #Rectangle es una funcion dibuja el rectangulo
        #El tercer argumento son las coordenadas de la parte inferior izquierda
        #del rectangulo
        #2 es el ancho de la linea del rectangulo
        cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0), 2)
        