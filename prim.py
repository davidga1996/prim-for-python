import copy



class Prim:
    def __init__(self, graph):
        #recogemos el grafo
        self.graph = graph
        #agregamos una lista vacia de aristas al grafo
        self.graph.prim = []



    def create(self):
        i = 0
        #tomamos el primer vertice
        vertex = self.graph.vertexs[i]
        while i < len(self.graph.vertexs) and len(self.graph.vertexs[i].edges) == 0:
            #en caso de que ese vertice no sea conexo
            #buscamos el siguiente
            i += 1
            vertex = self.graph.vertexs[i]

        weight = 1000 ** 3#modificar por uno mas optimo

        #caso inicial
        for e in vertex.edges:
            if e.weight < weight:
                #cambio de arista por la proxima mas pequeña
                edge = e

        #tomamos la arista y la agregamos al prim
        self.graph.prim.append(edge)
        #tambien creamos una lista que tomara los vetices visitados
        #con esto verificamos si ya se visitaron todas
        vertexs = []
        vertexs.append(edge.vo)
        vertexs.append(edge.vd)
    
        while len(self.graph.prim) < (len(self.graph.vertexs)-1) or len(vertexs) == len(self.graph.vertexs):
            #mientras no se esten todas las aristas
            #seguir buscando
            
            #reiniciar el peso al maximo posible
            weight = 1000 ** 3#modificar por uno mas optimo
            
            beforePrimSize = len(self.graph.prim)

            #creamos una copia de vertex, para iterar en ella
            vs = copy.copy(vertexs)

            for v in vs:
                #por cada vertice...
                for e in v.edges:
                    #por cada arista en mis vertices vicitados
                    if e.vd in vertexs:
                        #si mi vertice destino ya esta en
                        #la lista, no analaizarlo
                        continue
                    if e.weight < weight:
                        #si el peso es el menor de todos
                        #guardo la arista
                        edge = e

                if edge.vd not in vertexs:
                    #edge se pudo guardar en el recorrido anterior
                    #asi que debemos validar de nuevo

                    #despues de obtenerlo, guardamos la arista "con menos peso"
                    self.graph.prim.append(edge)
                    #tambien guardamos el vertice en las visitadas
                    vertexs.append(edge.vd)
                
            #comparacion de paro
            #si prim ya no crece, entonces detener el for
            if beforePrimSize == len(self.graph.prim):
                #esto sucede cuando hay al menos un vertice no conexo
                return



if __name__ == "__main__":
    print("ejecuta el archivo main.py")


