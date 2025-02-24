def liters_100km_to_miles_gallon(l_per_100km):
    return 235.214583 / l_per_100km

def miles_gallon_to_liters_100km(mpg):
    return 235.214583 / mpg

# Datos de prueba
valores_l_100km = [5, 7, 10]
valores_mpg = [47, 33.6, 23.5]

# Prueba
for i in range(len(valores_l_100km)):
    resultado_mpg = liters_100km_to_miles_gallon(valores_l_100km[i])
    if round(resultado_mpg, 2) == round(valores_mpg[i], 2):
        print(f"Test {i+1} (l/100km to mpg): Correcto")
    else:
        print(f"Test {i+1} (l/100km to mpg): Incorrecto")

for i in range(len(valores_mpg)):
    resultado_l_100km = miles_gallon_to_liters_100km(valores_mpg[i])
    if round(resultado_l_100km, 2) == round(valores_l_100km[i], 2):
        print(f"Test {i+1} (mpg to l/100km): Correcto")
    else:
        print(f"Test {i+1} (mpg to l/100km): Incorrecto")
