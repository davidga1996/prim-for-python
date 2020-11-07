from image import Image
from graph import Graph
from prim import Prim

if __name__ == "__main__":
    #cargamos la imagen
    image  = Image('img/mapa.png')
    #iniciamo el grafo "recibe la imagen"
    graph  = Graph(image)
    #creamos los vertices
    graph.createVertexs()
    #creamos las aristas
    graph.createEdges()
    #dibujamos las aristas "no necesario"
    graph.drawEdges()
    #dibujamos los vertices "no necesario"
    graph.drawVertexs()
    #al tener el grafo creado "vertices y aristas" toca cargar
    #el algoritmo de prim de ese grafo

    #iniciamos el algoritmo de prim
    prim = Prim(graph)

    #ejecutamos prim "aun no creado"
    prim.create()

    #prim cargar una lista de aristas al grafo
    #esta funcion dara error si no se ejecuta la linea 22
    #y dibujara el camino minimo
    graph.drawPrim()

    #al final mostramos el grafo final
    graph.showMap()