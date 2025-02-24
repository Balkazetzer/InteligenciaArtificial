def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

# Datos de prueba
anios = [2000, 1900, 2024, 2023, 2004]
resultados_esperados = [True, False, True, False, True]

# Prueba
for i in range(len(anios)):
    resultado = es_bisiesto(anios[i])
    if resultado == resultados_esperados[i]:
        print(f"Test {i+1}: Correcto")
    else:
        print(f"Test {i+1}: Incorrecto")
