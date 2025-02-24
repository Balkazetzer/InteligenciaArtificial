lista_original = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
lista_sin_repeticiones = []
for numero in lista_original:
    if numero not in lista_sin_repeticiones:
        lista_sin_repeticiones.append(numero)
print(lista_sin_repeticiones)
