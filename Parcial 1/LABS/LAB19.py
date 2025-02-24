beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    beatles.append(miembro)
del beatles[3]
del beatles[3]
beatles.insert(0, "Ringo Starr")
print("La formación final de The Beatles es:", beatles)