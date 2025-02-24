hora_inicio = int(input())
min_inicio = int(input())
duracion = int(input())
min_final = (min_inicio + duracion) % 60
hora_final = (hora_inicio + (min_inicio + duracion) // 60) % 24
print(hora_final, min_final)
