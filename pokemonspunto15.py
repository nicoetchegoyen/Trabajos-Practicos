entrenadores_pokemon = [
    ["Nicolas", 6, 4, 12,  [
        ["Kadabra", 18, "Psíquico", ""],
        ["Wartortle", 20, "Agua", ""],
        ["Raticate", 17, "Normal", ""],
        ["Pidgeotto", 18, "Normal", "Volador"],
    ]],
    ["Enzo", 13, 2, 39, [
        ["Tyrantrum", 66, "Roca", "Dragón"],
        ["Dragonite", 68, "Dragón", "Volador"],
        ["Gyarados", 64, "Agua", "Volador"],
        ["Charizard", 64, "Fuego", "Volador"],
        ["Dragonite", 70, "Dragón", "Volador"],
    ]],
    ["Fabio", 2, 2, 9, [
        ["Cradily", 56, "Roca", "Planta"],
        ["Armaldo", 56, "Roca", "Bicho"],
        ["Metagross", 61, "Acero", "Psíquico"],
        ["Claydol", 58, "Tierra", "Psíquico"],
        ["Skarmory", 57, "Acero", "Volador"],
    ]],
]

def cantidad_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            return len(entrenador_pokemon[4])
    return 0
print ("---------------------------------------------------------------------------------------------------")
print("Cantidad de Pokémons de Nicolas:", cantidad_pokemons("Nicolas"))


def tres_torneos_ganados():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[1] > 3:
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores
print("Entrenadores con más de tres torneos ganados:", tres_torneos_ganados())
print ("---------------------------------------------------------------------------------------------------")

def mejor_pokemon():
    mejor_entrenador = None
    max_torneos_ganados = -1
    for entrenador_pokemon in entrenadores_pokemon:
        torneos_ganados = entrenador_pokemon[1]
        if torneos_ganados > max_torneos_ganados:
            max_torneos_ganados = torneos_ganados
            mejor_entrenador = entrenador_pokemon

    if mejor_entrenador:
        pokemon_mayor_nivel = max(mejor_entrenador[4], key=lambda x: x[1])
        return pokemon_mayor_nivel
    return None
print("Pokémon de mayor nivel del mejor entrenador:", mejor_pokemon())
print ("---------------------------------------------------------------------------------------------------")

def entrenador_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            return entrenador_pokemon
    return None
print("Datos de Enzo y sus Pokémons:", entrenador_pokemons("Enzo"))
print ("---------------------------------------------------------------------------------------------------")

def porcentaje():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        total_batallas = entrenador_pokemon[2] + entrenador_pokemon[3]
        if total_batallas > 0:
            porcentaje_ganadas = (entrenador_pokemon[3] / total_batallas) * 100
            if porcentaje_ganadas > 79:
                entrenadores.append(entrenador_pokemon[0])
    return entrenadores
print("Entrenadores con porcentaje de batallas ganadas mayor al 79%:", porcentaje())
print ("---------------------------------------------------------------------------------------------------")

def entrenadores_tipo_fuego_planta_agua_volador(tipo, subtipo):
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if (pokemon[2] == tipo and pokemon[3] == subtipo) or (pokemon[2] == "Agua" and pokemon[3] == "Volador"):
                entrenadores.append(entrenador_pokemon[0])
                break
    return entrenadores
print("Entrenadores con Pokémons de tipo fuego y planta o agua/volador:")
print(entrenadores_tipo_fuego_planta_agua_volador("Fuego", "Planta") + entrenadores_tipo_fuego_planta_agua_volador("Agua", "Volador"))
print ("---------------------------------------------------------------------------------------------------")

def promedio_nivel_pokemons(entrenador):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == entrenador:
            pokemons = entrenador_pokemon[4]
            if len(pokemons) > 0:
                suma_niveles = sum([pokemon[1] for pokemon in pokemons])
                return suma_niveles / len(pokemons)
    return None
print("Promedio de nivel de los Pokémons de Azul:", promedio_nivel_pokemons("Azul"))
print ("---------------------------------------------------------------------------------------------------")

def cantidad_entrenadores_con_pokemon(pokemon_buscado):
    contador = 0
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if pokemon[0] == pokemon_buscado:
                contador += 1
                break
    return contador
print("Cantidad de entrenadores con el Pokémon 'Pikachu':", cantidad_entrenadores_con_pokemon("Pikachu"))
print ("---------------------------------------------------------------------------------------------------")

def pokemons_repetidos():
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        pokemons = entrenador_pokemon[4]
        nombres_pokemons = [pokemon[0] for pokemon in pokemons]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            entrenadores.append(entrenador_pokemon[0])
    return entrenadores
print("Entrenadores con Pokémons repetidos:", pokemons_repetidos())
print ("---------------------------------------------------------------------------------------------------")

def pokemons_consigna(pokemons_buscados):
    entrenadores = []
    for entrenador_pokemon in entrenadores_pokemon:
        for pokemon in entrenador_pokemon[4]:
            if pokemon[0] in pokemons_buscados:
                entrenadores.append(entrenador_pokemon[0])
                break
    return entrenadores
print("Entrenadores con Tyrantrum, Terrakion o Wingull:", pokemons_consigna(["Tyrantrum", "Terrakion", "Wingull"]))
print ("---------------------------------------------------------------------------------------------------")


def entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon):
    for entrenador_pokemon in entrenadores_pokemon:
        if entrenador_pokemon[0] == nombre_entrenador:
            for pokemon in entrenador_pokemon[4]:
                if pokemon[0] == nombre_pokemon:
                    return (entrenador_pokemon, pokemon)
    return None

print ("---------------------------------------------------------------------------------------------------")

resultado = entrenador_tiene_pokemon("Nicolas", "Pidgeotto")
if resultado:
    entrenador, pokemon = resultado
    print("k. Nicolas tiene a 'Pidgeotto':")
    print("Nombre del entrenador:", entrenador[0])
    print("Cantidad de torneos ganados:", entrenador[1])
    print("Cantidad de batallas perdidas:", entrenador[2])
    print("Cantidad de batallas ganadas:", entrenador[3])
    print("Datos del Pokémon:")
    print("Nombre:", pokemon[0])
    print("Nivel:", pokemon[1])
    print("Tipo:", pokemon[2])
    print("Subtipo:", pokemon[3])
else:
    print("k. Nicolas no tiene a 'Pidgeotto'.")
    
print ("---------------------------------------------------------------------------------------------------")

