def calcular_altura_piramide(bloques):
    altura = 0
    bloques_necesarios = 0
    
    while True:
        altura += 1
        bloques_necesarios += altura
        
        if bloques_necesarios > bloques:
            altura -= 1
            break
        elif bloques_necesarios == bloques:
            break
    
    return altura

# Prueba con los datos proporcionados
bloques = 6
altura = calcular_altura_piramide(bloques)
print(f"Con {bloques} bloques, la altura de la pirámide es: {altura}")