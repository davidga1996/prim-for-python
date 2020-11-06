import cv2
import numpy as np



class Image:
    def __init__(self, img):
        #recibvimos la dereccion de la imagen
        #y creamos el mapa de bits
        self.image      = cv2.imread(img)
        #generamos una imagen nueva "a escala de grises"
        self.imageCopy  = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        #obtengo un binarizacion en blaco todos lo pixeles cuyo valor en sea entre 254 y 255
        #convierte la imagen en B/W
        _, self.imageCopy  = cv2.threshold(self.imageCopy, 254, 255, cv2.THRESH_BINARY)
        
        #creamos un kernel de 11x11
        self.kernel     = np.ones((11,11), np.uint8)




    def convertToBAW(self):
        #filtro de dilatacion
        self.imageCopy = cv2.dilate(self.imageCopy, self.kernel, 1)
        #Despues aplico uno de erosion
        self.imageCopy = cv2.erode(self.imageCopy, self.kernel, 1)
        #aplico un flitro gausiando, para suavisar los bordes 
        self.imageCopy = cv2.GaussianBlur(self.imageCopy, (5,5), cv2.BORDER_DEFAULT) 
        


    def harris(self):
        #Aplico la deteccion de Esquinas de Harris
        self.dst = cv2.cornerHarris(self.imageCopy, 2, 3, 0.05)
        _, self.dst = cv2.threshold(self.dst, 0.04*self.dst.max(), 255, 0)
        self.dst = np.uint8(self.dst)
        _,self.imageCopy = cv2.threshold(self.imageCopy,235,255,cv2.THRESH_BINARY)
        self.imageCopy = cv2.dilate(self.imageCopy,self.kernel,1)
        #aqui devuelvo la imagen binarizada a tres canales
        self.imageCopy = cv2.cvtColor(self.imageCopy,cv2.COLOR_GRAY2BGR)


if __name__ == "__main__":
    print("ejecuta el archivo main.py")