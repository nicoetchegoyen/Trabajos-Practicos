"""14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
guientes tareas:

a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
ta es la distancia entre los ambientes, se debe cargar en metros;

c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
para conectar todos los ambientes;

d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el
Smart Tv."""

from grafo import Grafo 
from lista import Lista as ListaArista
from cola import Cola
from pila import Pila
from heap_min import Heap

mi_grafo = Grafo(dirigido=False)
#a. insertar los vertices del grafo
mi_grafo.insert_vertice('cocina')
mi_grafo.insert_vertice('comedor')
mi_grafo.insert_vertice('cochera')
mi_grafo.insert_vertice('quincho')
mi_grafo.insert_vertice('baño1')
mi_grafo.insert_vertice('baño2')
mi_grafo.insert_vertice('habitacion1')
mi_grafo.insert_vertice('habitacion2')
mi_grafo.insert_vertice('sala_de_estar')
mi_grafo.insert_vertice('terraza')
mi_grafo.insert_vertice('patio')
#b. insertar las aristas del grafo
mi_grafo.insert_arist('cocina', 'comedor', 5)
mi_grafo.insert_arist('cocina', 'cochera', 5)
mi_grafo.insert_arist('cocina', 'quincho', 8)
mi_grafo.insert_arist('comedor', 'cochera', 5)
mi_grafo.insert_arist('comedor', 'quincho', 5)
mi_grafo.insert_arist('comedor', 'baño1', 2)
mi_grafo.insert_arist('cochera', 'quincho', 5)
mi_grafo.insert_arist('cochera', 'baño1', 5)
mi_grafo.insert_arist('cochera', 'baño2', 8)
mi_grafo.insert_arist('quincho', 'baño1', 5)
mi_grafo.insert_arist('quincho', 'baño2', 5)
mi_grafo.insert_arist('quincho', 'habitacion1', 4)
mi_grafo.insert_arist('baño1', 'baño2', 5)
mi_grafo.insert_arist('baño1', 'habitacion1', 5)
mi_grafo.insert_arist('baño1', 'habitacion2', 3)
mi_grafo.insert_arist('baño2', 'habitacion1', 5)
mi_grafo.insert_arist('baño2', 'habitacion2', 5)
mi_grafo.insert_arist('baño2', 'sala_de_estar', 2)
mi_grafo.insert_arist('habitacion1', 'habitacion2', 5)
mi_grafo.insert_arist('habitacion1', 'sala_de_estar', 5)
mi_grafo.insert_arist('habitacion1', 'terraza', 4)
mi_grafo.insert_arist('habitacion2', 'sala_de_estar', 5)
mi_grafo.insert_arist('habitacion2', 'terraza', 5)
mi_grafo.insert_arist('habitacion2', 'patio', 8)
mi_grafo.insert_arist('sala_de_estar', 'terraza', 5)
mi_grafo.insert_arist('sala_de_estar', 'patio', 5)
mi_grafo.insert_arist('sala_de_estar', 'cocina', 8)
mi_grafo.insert_arist('terraza', 'patio', 5)
mi_grafo.insert_arist('terraza', 'cocina', 5)
mi_grafo.insert_arist('terraza', 'comedor', 8)
mi_grafo.insert_arist('patio', 'cocina', 5)
mi_grafo.insert_arist('patio', 'comedor', 5)
mi_grafo.insert_arist('patio', 'cochera', 8)

#c. imprimir el arbol de expansion minima dado por el metodo de kruskal
bosque = mi_grafo.kruskal()
for arbol in bosque:
    print("---------------------------------------------------------------------------------")
    print('c.arbol de expansion minima:')
    for nodo in arbol.split(';'):
        print(nodo)
#c. definimos funcion para la cantidad total de metros de cable necesaria (sumando las aristas del arbol de expansion minima)
def cantidad_cables():
    total_cables=0
    bosque=mi_grafo.kruskal()
    for arbol in bosque:
        print ('')
        for nodo in arbol.split(';'):
            partes=nodo.split('-')
            peso=int(partes[-1])
            total_cables+=peso
    print(f'la longitud total de los cables necesarioes es de: {total_cables} metros')

cantidad_cables()


#d. incompleto o mal, esta es la unica forma que encontre de darle sentido al programa para buscar el camino mas corto
ori = 'habitacion1'
des = 'sala_de_estar'
origen = mi_grafo.search_vertice(ori)
destino = mi_grafo.search_vertice(des)
camino_mas_corto = None
if(origen is not None and destino is not None):
    if(mi_grafo.has_path(ori, des)):
        camino_mas_corto = mi_grafo.dijkstra(ori, des)
        fin = des
        while camino_mas_corto.size() > 0: 
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print("---------------------------------------------------------------------------------")
                print("d.Se deberia instalar un cable desde", ori, "hasta", des, "de", value[1], "metros")  
                print("---------------------------------------------------------------------------------")     

    


