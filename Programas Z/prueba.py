beatles = []
print("Paso 1:", beatles)
beatles.append("Jhon Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# paso 2
print("Paso 2:", beatles)
for x in range(2):
    beatles.append(input("Di el nombre de otro integrante: "))
    

# paso 3
print("Paso 3:", beatles)
del beatles[-1]
del beatles[-1]
# paso 4
print("Paso 4:", beatles)

beatles.insert(0, "Ringo Starr")
# paso 5
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))




