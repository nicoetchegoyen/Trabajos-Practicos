from cola import Cola

personajes_mcu = Cola()
personajes_mcu.arrive({'nombre': 'Tony Stark', 'superheroe': 'Iron Man', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Steve Rogers', 'superheroe': 'Capitan America', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Natasha Romanoff', 'superheroe': 'Black Widow', 'genero': 'F'})
personajes_mcu.arrive({'nombre': 'Carol Danvers', 'superheroe': 'Capitana Marvel', 'genero': 'F'})
personajes_mcu.arrive({'nombre': 'Scott Lang', 'superheroe': 'Ant-Man', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Peter Parker', 'superheroe': 'Spider-Man', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Stephen Strange', 'superheroe': 'Doctor Strange', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Thor Odinson', 'superheroe': 'Thor', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Bruce Banner', 'superheroe': 'Hulk', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Wanda Maximoff', 'superheroe': 'Scarlet Witch', 'genero': 'F'})
personajes_mcu.arrive({'nombre': 'Peter Quill', 'superheroe': 'Star-Lord', 'genero': 'M'})
personajes_mcu.arrive({'nombre': 'Gamora', 'superheroe': 'Gamora', 'genero': 'F'})
personajes_mcu.arrive({'nombre': 'Vision', 'superheroe': 'Vision', 'genero': 'M'})


def obtener_nombre_capitana_marvel(cola):
    nombre_capitana_marvel = None

    cont = 0
    total = cola.size()
    while cont < total:
        personaje = cola.on_front()
        if personaje['superheroe'] == 'Capitana Marvel':
            nombre_capitana_marvel = personaje['nombre']
            break
        cola.move_to_end()
        cont += 1

    return nombre_capitana_marvel

nombre_capitana_marvel = obtener_nombre_capitana_marvel(personajes_mcu)
print("Nombre del personaje de la superheroe Capitana Marvel:", nombre_capitana_marvel)

def mostrar_superheroes_femeninos(cola):
    superheroes_femeninos = []

    cont = 0
    total = cola.size()
    while cont < total:
        personaje = cola.on_front()
        if personaje['genero'] == 'F':
            superheroes_femeninos.append(personaje['superheroe'])
        cola.move_to_end()
        cont += 1

    print("-----------------------------------------------------------------------------")
    print("Nombres de los superheroes femeninos:")
    print("-----------------------------------------------------------------------------")
    for heroe in superheroes_femeninos:
        print(heroe)

mostrar_superheroes_femeninos(personajes_mcu)

def mostrar_personajes_masculinos(cola):
    personajes_masculinos = []

    cont = 0
    total = cola.size()
    while cont < total:
        personaje = cola.on_front()
        if personaje['genero'] == 'M':
            personajes_masculinos.append(personaje['nombre'])
        cola.move_to_end()
        cont += 1

    print("-----------------------------------------------------------------------------")
    print("Nombres de los personajes masculinos:")
    print("-----------------------------------------------------------------------------")
    for personaje in personajes_masculinos:
        print(personaje)

mostrar_personajes_masculinos(personajes_mcu)

def obtener_superheroe_scott_lang(cola):
    superheroe_scott_lang = None

    cont = 0
    total = cola.size()
    while cont < total:
        personaje = cola.on_front()
        if personaje['nombre'] == 'Scott Lang':
            superheroe_scott_lang = personaje['superheroe']
            break
        cola.move_to_end()
        cont += 1

    return superheroe_scott_lang

superheroe_scott_lang = obtener_superheroe_scott_lang(personajes_mcu)
print("-----------------------------------------------------------------------------")
print("Nombre del superheroe del personaje Scott Lang:", superheroe_scott_lang)
print("-----------------------------------------------------------------------------")

def mostrar_personajes_con_letra_s(cola):
    personajes_letra_s = []

    cont = 0
    total = cola.size()
    while cont < total:
        personaje = cola.on_front()
        if personaje['nombre'].startswith('S'):
            personajes_letra_s.append(personaje)
        cola.move_to_end()
        cont += 1

    print("-----------------------------------------------------------------------------")
    print("Datos de los superheroes o personajes cuyos nombres comienzan con la letra S:")
    print("-----------------------------------------------------------------------------")
    for personaje in personajes_letra_s:
        print(personaje)

mostrar_personajes_con_letra_s(personajes_mcu)

def verificar_carol_danvers(cola):
    carol_danvers_en_cola = False
    nombre_superheroe_carol_danvers = None

    cont = 0
    total = cola.size()
    while cont < total:
        personaje = cola.on_front()
        if personaje['nombre'] == 'Carol Danvers':
            carol_danvers_en_cola = True
            nombre_superheroe_carol_danvers = personaje['superheroe']
            break
        cola.move_to_end()
        cont += 1

    if carol_danvers_en_cola:
        print("-----------------------------------------------------------------------------")
        print("El personaje Carol Danvers se encuentra en la cola.")
        print("Nombre de su superheroe:", nombre_superheroe_carol_danvers)
        print("-----------------------------------------------------------------------------")
    else:
        print("-----------------------------------------------------------------------------")
        print("El personaje Carol Danvers no se encuentra en la cola.")
        print("-----------------------------------------------------------------------------")

verificar_carol_danvers(personajes_mcu)
