def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):

    if indice >= len(mochila):
        return -1
    elif mochila[indice] == 'sable de luz':
        return objetos_sacados + 1
    else:
        return usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)

mochila = ['botas', 'comida', 'agua', 'sable de luz', 'medicina']
objetos_sacados = usar_la_fuerza(mochila)
if objetos_sacados == -1:
    print("No se encontró el sable de luz en la mochila.")
else:
    print("Se sacaron", objetos_sacados, "objetos para encontrar el sable de luz.")