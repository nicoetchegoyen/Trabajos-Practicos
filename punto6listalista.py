superheroes = [
    ["Linterna Verde", 1940, "DC", "es un superhéroe que usa un anillo de poder para crear construcciones de luz sólida."],
    ["Wolverine", 1974, "Marvel", "un mutante con garras retractables y una capacidad de regeneración asombrosa."],
    ["Dr. Strange", 1963, "DC", "es un hechicero supremo del Universo Marvel."],
    ["Iron Man", 1963, "Marvel", "es un superhéroe multimillonario cuya identidad secreta es Tony Stark. Usa un traje de alta tecnología para luchar contra el crimen."],
    ["Flash", 1940, "DC", "es un superhéroe con la capacidad de correr a velocidad de la luz."],
    ["Star-Lord", 1976, "Marvel", "es el líder de los Guardianes de la Galaxia en el Universo Marvel."],
    ["Capitana Marvel", 1967, "Marvel", "es una superhéroe de Marvel con poderes cósmicos."],
    ["Mujer Maravilla", 1941, "DC", "es una princesa amazona con habilidades sobrehumanas."],
    ["Superman", 1938, "DC", "es un superhéroe ficticio creado por Jerry Siegel y Joe Shuster."],
]

superheroes = [superheroe for superheroe in superheroes if superheroe[0] != "Linterna Verde"]
print("-------------------------------------------------------------------------------")
print ("ATENCION: Tras el ataque de Thanos, se perdio todo registro de Linterna Verde")

print("-------------------------------------------------------------------------------")
for superheroe in superheroes:
    if superheroe[0] == "Wolverine":
        print(f"Wolverine aparece en el año {superheroe[1]}")
print("-------------------------------------------------------------------------------")

for superheroe in superheroes:
    if superheroe[0] == "Dr. Strange":
        superheroe[2] = "Marvel"
        print ("***!Ahora Dr. Strange es de Marvel¡***")

for superheroe in superheroes:
    if "traje" in superheroe[3] or "armadura" in superheroe[3]:
        print(f"Superhéroe con traje o armadura en su biografia: {superheroe[0]}, {superheroe[3]}")
print("-------------------------------------------------------------------------------")


print ("Superheroes que aparecieron antes de 1963")
for superheroe in superheroes:
    if superheroe[1] < 1963:
        print(f"{superheroe[0]}, Casa: {superheroe[2]}")
print("-------------------------------------------------------------------------------")


for superheroe in superheroes:
    if superheroe[0] == "Capitana Marvel" or superheroe[0] == "Mujer Maravilla":
        print(f"{superheroe[0]}, Casa: {superheroe[2]}")
print("-------------------------------------------------------------------------------")
    

print ("Informacion acerca de Flash y Star Lord")
for superheroe in superheroes:
    if superheroe[0] == "Flash" or superheroe[0] == "Star-Lord":
        print(f"{superheroe[0]} aparecio en {superheroe[1]}, de la casa {superheroe[2]}, {superheroe[3]}")

print("-------------------------------------------------------------------------------")


print ("Superheroes que empiezan con B, M o S")
letras_filtro = ["B", "M", "S"]
for superheroe in superheroes:
    if superheroe[0][0] in letras_filtro:
        print(f"{superheroe[0]}")
print("-------------------------------------------------------------------------------")


conteo_dc = 0
conteo_marvel = 0

for superheroe in superheroes:
    if superheroe[2] == "DC":
        conteo_dc += 1
    elif superheroe[2] == "Marvel":
        conteo_marvel += 1

print("-------------------------------------------------------------------------------")
print(f"Hay {conteo_dc} superheroes de DC")
print(f"Hay {conteo_marvel} superheroes de MARVEL")
print("-------------------------------------------------------------------------------")
