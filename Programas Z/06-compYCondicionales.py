# ==   !=    >    <   >= <=
# 

var = 0  # Asignando 0 a var
print(var == 0)

var = 1  # Asignando 1 a var
print(var == 0)
#  var = 0  # Asignando 0 a var
var = 0
print(var != 0)
 
var = 1  # Asignando 1 a var
print(var != 0) 

print("----------")
n = int(input("Ingresa un numero: "))
print(n>=100)
print("----------------------")

var=5
if var > n:
    print("Entra en el if")
else:
    print("Entra en el else")
print("Esto lo imprime siempre")

#elif es una forma de if que ejecutará la primera opcion correcta que encuentre, se puede acabar con un else para cub
#cubrir el resto de opciones
z = 3

if z == 1:
    print("var = 1")
elif z == 2:
    print("var = 2")
elif z == 3:
    print("var = 3")
elif z == 4:
    print("var = 4")
else:
    print("El Valor de Z es: ",z)


print("---------------------------------------")
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

print("------------------------------------------")
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

if number1 > number2:
    if number1 > number3: largest_number = number1
    else: largest_number = number3
else:
    if number2 > number3: largest_number = number2
    else: largest_number = number3
# Imprime el resultado.
print("El número más grande es:", largest_number)

entrada = input()
if entrada == "ESPATIFILIO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif entrada == "espatifilio":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No " + entrada + "!")



print("--------------------")
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
elif income > 85528:
    tax = 14839.02 + ((income - 85528)*0.32)

if tax < 0:
    tax = .0
else:
    tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
 

print("------------------------------")
anio = input("Introduce el año: ")

if anio < 1582:
    tipo_anio = "noGregoriano"
elif anio%4 != 0:
    tipo_anio = "Comun"
elif anio%100 != 0:
    tipo_anio = "bisiesto"
elif anio%400 != 0:
    tipo_anio = "Comun"
else:
    tipo_anio = "bisiesto"

if tipo_anio == "noGregoriano":
    print("Este es un año fuera del periodo Gregoriano")
else:
    print("Año " + tipo_anio)




