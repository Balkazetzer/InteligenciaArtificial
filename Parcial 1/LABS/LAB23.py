import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Datos de prueba
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
resultados_esperados = [True, True, False, True, False, True, False, False, False]

# Prueba
for i in range(len(numeros)):
    resultado = is_prime(numeros[i])
    if resultado == resultados_esperados[i]:
        print(f"Test {i+1}: Correcto")
    else:
        print(f"Test {i+1}: Incorrecto")
