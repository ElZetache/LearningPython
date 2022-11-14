print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")
print("-------------------------------------")
#El input siempre devuelve un string, por eso no podemos hacer operaciones matematicas directamente con el, pero podemos convertirlo con int(), float()...
anything = float(input("Ingresa un número:"))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

print("-------------------------------------")
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)
#si queremos concadenar con el simbolo + tenemos que convertir los numericos a Strings, esto lo podemos hacer con str()
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))


var_a = float(input("Inserta el valor a:"))
var_b = float(input("Inserta el valor b:"))

print("Suma: " + str(var_a + var_b))
print("Resta: " +str(var_a - var_b))
print("Multiplicacion: " + str(var_a * var_b))
print("Division: " + str(var_a / var_b))

print("\n¡Eso es todo, amigos!")
print("-------------------------------------------------")
x = float(input("Ingresa el valor para x: "))

y =  1/(x+(1/(x+(1/(x+(1/x))))))     

print("y =", y)



hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

calc_min_tot = mins + dura
sobrante_min = calc_min_tot % 60
calc_hora = hour + (calc_min_tot // 60) - (24*((hour + (calc_min_tot // 60))//24))


hora_final =  str(calc_hora) +  ":" + str(sobrante_min)

print(hora_final)


#se puede usar el input como pausa o para terminar un programa
print("\nPresiona Enter para terminar el programa.")
input()
print("FIN.")
