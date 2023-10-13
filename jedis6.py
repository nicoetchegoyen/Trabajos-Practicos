"""6. Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos

tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
siguientes consignas:
a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
b. realizar un barrido inorden del árbol por nombre y ranking;
c. realizar un barrido por nivel de los árboles por ranking y especie;
d. mostrar toda la información de Yoda y Luke Skywalker;
e. mostrar todos los Jedi con ranking “Jedi Master”;
f. listar todos los Jedi que utilizaron sabe de luz color verde;
g. listar todos los Jedi cuyos maestros están en el archivo;
h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre."""

from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open("jedis.txt", "r")
read_lines = file_jedi.readlines()
file_jedi.close()

#a.
name_tree = BinaryTree()
specie_tree = BinaryTree()
ranking_tree = BinaryTree()

read_lines.pop(0)
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';')
    jedi.pop() 
    name_tree.insert_node(jedi[0], index+2)
    specie_tree.insert_node(jedi[2], index+2)
    ranking_tree.insert_node(jedi[1], index+2)

print("---------------------------------")
print("b. Barrido por nombre y ranking")
name_tree.inorden_file('jedis.txt')
print()
ranking_tree.inorden_file('jedis.txt')

print("---------------------------------")
print("c. Barrido por ranking y especie")
ranking_tree.by_level()
print()
specie_tree.by_level()
print("---------------------------------")


print("d.")
print("YODA.INFO:")
pos = name_tree.search('yoda')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')
print("")
print("SKYWALKER.INFO")
pos = name_tree.search('luke skywalker')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no esta en la lista')

print("---------------------------------")

print("e. JEDIS MASTERS")
name_tree.inorden_maestros('jedis.txt')

print("---------------------------------")

print("f.JEDIS CON SABLE COLOR VERDE")
name_tree.inorden_file_lightsaber('jedis.txt', 'green')
print("---------------------------------")

#g. listar todos los Jedi cuyos maestros están en el archivo;


print("h. Togruta")
pos = specie_tree.search('togruta')
if pos:
    print(get_value_from_file('jedis.txt', pos.other_values))
else:
    print('no Togruta')
print("---------------------------------")
print("")




print("i.JEDIS QUE EMPIEZAN CON 'A'")
name_tree.inorden_start_with_jedi('A')
print("")
