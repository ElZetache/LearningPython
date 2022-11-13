#en python tenemos dos funciones min() y max() que devuelven el numero mayor o menor entre todos los 
#que le pasemos
print(max(2,6,3,9,5))
print(min(4,6,3,9,5))
print("----------------------")

 # Almacena el actual número más grande aquí.
largest_number = -999999999
 
# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))
 
# Imprime el número más grande.
print("El número más grande es:", largest_number)

print("------------------------------------------------------------------")
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
print("----------------------------------------")
secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
numero_user = int(input("introduce un numero:"))
while numero_user != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero_user = int(input("introduce otro numero:"))
print(str(numero_user) + " ¡Bien hecho, muggle! Eres libre ahora.")


print("-------------------------------------")
for i in range(10):
    print("El valor de i es", i)
#podemos asignar a i un valor inicial y decirle en cual acabar
for i in range(2, 8):
    print("El valor de i es", i)
#si se le añade un tercer argumento este será el incremento 
for i in range(2, 8, 3):
    print("El valor de i es", i)
print("-----------------------------------------")
import time

for i in range (1,6):
    print(str(i) + " missisipi")
    time.sleep(1)

# Escribe una función print con el mensaje final.
print("Final del conteo")


print("-------------------------------")
#aunque no se lo mas correcto a nivel purista de programacion existen las sentencias break y continue
#para modificar el curso de un bucle

palabra_secreta = "chupacabra"

while True:
    user_word = input("Ingresa la palabra secreta: ")
    if user_word == palabra_secreta:        
        break
print("Has dejado el bucle con exito")
    
print("------------------------------------------------")

user_word = input("Introduce una palabra: ")
user_word = user_word.upper()
word_without_vowels = ""

#Gregory
for letter in user_word:
    if letter == "A":        
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)


blocks = int(input("Ingresa el número de bloques: "))
bloques_restantes = blocks
bloques_para_siguiente_capa = 1
numero_capas = 0

while bloques_restantes >= bloques_para_siguiente_capa:
    numero_capas += 1
    bloques_restantes = bloques_restantes - bloques_para_siguiente_capa
    bloques_para_siguiente_capa += 1
height = numero_capas


print("La altura de la pirámide:", height)


print("------------------------------------------")

c0 = int(input("Introduce un numero positivo: "))
pasos = 0

while c0 == 1:
    if c0 % 2:
        c0 = c0 / 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    pasos += 1
print("El numero de pasos es: ", pasos)








 
