#en python para crear una variable no hay que declararla, solo hay que asignarle un valor
cantidad_fruta = 2
fruta = "manzanas"
print("tengo",cantidad_fruta,fruta)
cantidad_fruta = cantidad_fruta + 2
fruta = "peras"
print("tengo",cantidad_fruta,fruta)
print("----------------------")
john = 3 
mary = 5
adam = 6
manzanas_totales = john + mary + adam
print("Numero total de manzanas:",manzanas_totales)
print("----------------------")

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
print("----------------------")
print("----------------------")
x =  -1
x = float(x)
y = (3*x**3)-(2*x**2)+(3*x)-1
print("y =", y)
