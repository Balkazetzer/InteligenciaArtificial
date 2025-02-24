# Lista inicial
sombrero = [1, 2, 3, 4, 5]

# Paso 1: Reemplazar el número central
nuevo_numero = int(input("Ingresa un número entero para reemplazar el número central: "))
sombrero[2] = nuevo_numero

# Paso 2: Eliminar el último elemento
sombrero.pop()

# Paso 3: Imprimir la longitud de la lista
print("La longitud de la lista es:", len(sombrero))