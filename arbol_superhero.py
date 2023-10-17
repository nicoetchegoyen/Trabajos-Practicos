"""Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol. pag 158"""

from arbol_binario import BinaryTree

lista_heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': True},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': True},
    {'name': 'cbum', 'heroe': True},
    {'name': 'cro', 'heroe': True},
    {'name': 'colo', 'heroe': True},
    ]

arbol = BinaryTree()

for heroe in lista_heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'])

print("--------------------")
print("b. Villanos ordenados alfabeticamente:")
arbol.inorden_super_or_villano(False)



print("--------------------")
print("c. superheroes que empiezan con C:")
arbol.search_by_coincidence('c')



print("--------------------")
print('d. Cantidad de superheroes', arbol.contar_heroes())
print("--------------------")

value = input('e. Ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
    is_hero = pos.other_values
    arbol.delete_node(value)
    print('modificar')
    new_value = input('ingrese en nuevo nombre ')
    arbol.insert_node(new_value, is_hero)
else:
    print('no esta')
print()

# arbol.inorden()
# print("--------------------")
arbol.by_level()
print("--------------------")


def inorden_descendente(root):
    if root is not None:
        inorden_descendente(root.right) 
        if root.other_values: 
            print(root.value)  
        inorden_descendente(root.left)

print("--------------------")
print("f.Nombres de superhéroes en orden descendente:")
inorden_descendente(arbol.root)
print("--------------------")




