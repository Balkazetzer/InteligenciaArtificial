def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

def dia_del_anio(anio, mes, dia):
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if mes < 1 or mes > 12 or dia < 1 or dia > dias_por_mes[mes - 1] or (mes == 2 and dia == 29 and not es_bisiesto(anio)):
        return None
    
    if mes > 2 and es_bisiesto(anio):
        dia += 1
    
    return sum(dias_por_mes[:mes - 1]) + dia

# Datos de prueba
fechas = [(2024, 2, 29), (2023, 2, 29), (2020, 3, 1), (2025, 12, 31), (2021, 4, 31)]
resultados_esperados = [60, None, 61, 365, None]

# Prueba
for i in range(len(fechas)):
    resultado = dia_del_anio(fechas[i][0], fechas[i][1], fechas[i][2])
    if resultado == resultados_esperados[i]:
        print(f"Test {i+1}: Correcto")
    else:
        print(f"Test {i+1}: Incorrecto")
