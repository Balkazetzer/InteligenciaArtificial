def conjetura_collatz(c0):
    pasos = 0  # Contador de pasos
    print(f"Valor inicial: {c0}")
    
    while c0 != 1:
        if c0 % 2 == 0:  # Si es par
            c0 = c0 // 2
        else:  # Si es impar
            c0 = 3 * c0 + 1
        pasos += 1
        print(f"Paso {pasos}: {c0}")
    
    print(f"\nSe alcanzó 1 en {pasos} pasos.")

# Prueba del programa
try:
    c0 = int(input("Ingresa un número natural (mayor que 0): "))
    if c0 <= 0:
        print("El número debe ser mayor que 0.")
    else:
        conjetura_collatz(c0)
except ValueError:
    print("Entrada inválida. Debes ingresar un número entero.")