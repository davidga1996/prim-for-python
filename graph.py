import cv2
import numpy as np
from math import sqrt



class Graph:
    def __init__(self, img):
        self.imgo = img
        self.imgf = None
        self.vertexs = []

    def createVertexs(self):
        self.imgo.convertToBAW()
        self.imgo.harris()
        _, _, _, centroids = cv2.connectedComponentsWithStats(self.imgo.dst, 30, cv2.CV_32S)
        #self.vertexs = np.int0(centroids)
        for v in np.int0(centroids):
            vertex = Vertex(v[0], v[1])
            self.vertexs.append(vertex)

    def createEdges(self):
        #solo crea aristas en las que pasen solo por la calle
        for h in range(len(self.vertexs)):
            i=self.vertexs[h]
            for k in range(h,len(self.vertexs)):
                j=self.vertexs[k]
                if not i == j:
                    #evitamos unir uno consigo mismo
                    if self.ddaConnect(i, j):
                        #con el algoritmo dda validamos que
                        #solo pase por la calle

                        #creamos la arista (i -> j) "una direccion"
                        self.vertexs[h].addEdge(Edge(i, j))

                        #creamos la arista (j -> i) "una direccion"
                        self.vertexs[k].addEdge(Edge(j, i))
        #guardo la imagen generada para podre trabajar sobre ella
        self.imgf = self.imgo.imageCopy


    def ddaConnect(self, v1, v2):
        #con el algorimo DDA buscamos pixel por pixel
        x1 = v1.value['x']
        y1 = v1.value['y']
        x2 = v2.value['x']
        y2 = v2.value['y']

        if(abs(x2 - x1) >= abs(y2 - y1)):
            res = abs(x2 - x1)
        else:
            res = abs(y2 - y1)
        
        ax = (x2 - x1) / res
        ay = (y2 - y1) / res
        x = float(x1)
        y = float(y1)
        
        i = 0

        while(i <= res):
            if self.isBlack(int(x), int(y)):
                #si se encuentra un pixel negro dejar de buscar
                #y decir que no es una coneccion valida
                return False
            x += ax
            y += ay
            i+=1

        return True


    def isBlack(self, x, y):
        return self.imgo.imageCopy[y, x][0] == 0 and self.imgo.imageCopy[y, x][1] == 0 and self.imgo.imageCopy[y, x][2] == 0
 

    def drawVertexs(self):
        for p in self.vertexs:
            cv2.circle(self.imgf, (p.value['x'], p.value['y']), 5, (255,0,0), -1)    
        cv2.waitKey(1)

    def drawEdges(self):
        for v in self.vertexs:
            for e in v.edges:
                cv2.line(self.imgf, (e.vo.value['x'], e.vo.value['y']), (e.vd.value['x'], e.vd.value['y']), (0,255,0), 1)


    def drawPrim(self):
        for e in self.prim:
            cv2.line(self.imgf, (e.vo.value['x'], e.vo.value['y']), (e.vd.value['x'], e.vd.value['y']), (0,0,255), 1)


    def showMap(self):
        cv2.imshow('mapa',self.imgf)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



class Vertex:
    def __init__(self, x, y):
        self.value = {'x': x, 'y': y }
        self.edges = []


    def addEdge(self, edge):
        self.edges.append(edge)

    def __str__(self):
        return "[" + str(self.value['x']) + ", " + str(self.value['y']) + "]"


class Edge:
    def __init__(self, vo, vd):
        self.vo = vo
        self.vd = vd
        self.weight = distance(vo, vd)

    def __str__(self):
        o = str(self.vo.value['x']) + ":" + str(self.vo.value['y'])
        d = str(self.vd.value['x']) + ":" + str(self.vd.value['y'])
        return "[" + o + ", " + d  + " -> " + str(self.weight) + "]"

    def __repr__(self):
        return "\n" + self.__str__()

def distance(vo, vd):
    x1 = vo.value['x']
    y1 = vo.value['y']
    x2 = vd.value['x']
    y2 = vd.value['y']

    return sqrt(
        abs(x1 - x2) ** 2 +
        abs(y1 - y2) ** 2
    )


if __name__ == "__main__":
    print("ejecuta el archivo main.py")