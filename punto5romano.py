def romano_a_decimal(num_romano):
    valores = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if len(num_romano) == 0:
        return 0

    if len(num_romano) == 1:
        return valores[num_romano]

    if valores[num_romano[0]] < valores[num_romano[1]]:
        return valores[num_romano[1]] - valores[num_romano[0]] + romano_a_decimal(num_romano[2:])
    else:
        return valores[num_romano[0]] + romano_a_decimal(num_romano[1:])

num_romano = input("Ingrese un numero romano").upper()

num_decimal = romano_a_decimal(num_romano)
print("El numero decimal correspondiente a", num_romano, "es:", num_decimal)

