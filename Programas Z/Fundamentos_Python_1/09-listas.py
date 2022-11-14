numbers = [10, 5, 7, 2, 1]
print("Lista: ", numbers)

numbers[0] = 111
print("Lista: ", numbers)

numbers[1] = numbers[4]
print("Lista: ", numbers)

print(numbers[0])
print(len(numbers))

#Las listas en Python son variables, podemos eliminar o añadir elementos, esto modifica tambien
#la longitud de la lista:
del numbers[1]
print(len(numbers))

#En python podemos poner indices negativos en las listas, estos harán que se empiece a contar
#desde el final:
print(numbers[-1]) #cogería el ultimo elemento de la lista
print(numbers[-2]) #cogería el penultimo elemento de la lista

#con el metodo append añadimos un elemento al final de una lista:
numbers.append(5)
print(numbers)
#con el metodo insert hacemos lo mismo pero ademas podemos elegir en que posicion de la lista 
#añadimos este elemento
numbers.insert(1, 5)
print(numbers)
#con estos metodos podemos crear una lista vacia e irla llenando segun necessitemos
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
# con el for podemos recorrer una lista de la siguiente manera:
#esto recorre toda la lista y va asicnando a z los valores de la misma
for z in my_list:
    print(z)
#Python permite hacer mas de una asignacion a la vez
variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1
