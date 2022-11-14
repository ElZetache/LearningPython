#dato importante sobre las listas, las listas apuntan a una ubicacion de memoria
#por lo que si asignamos una a otra no estamos pasandole sus valores
#sino su ubicacion en la memoria, por lo que lo que hagas en una afectará a la otra
list_1 = [1]
list_2 = list_1
list_1[0] = 2 #modificamos la lista 1
print(list_2) #afecta a la lista 2
#para dar solucion a esto tenemos lo que se le llama "rebanadas":
#en este caso si que se copia y genera una lista nueva a partir del rango que le especiques
# en este caso pasara desde el elemento [1] de la lista hasta llegar al [3] (el ultimo no se incluye)
#si ponemos solo [:] se copian todos los datos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
#si recordamos el uso de indices negativos si ponemos que coja has -1 cogerá hasta el ultimo
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list) 
#las rebanadas tambien se pueden usar con el del para eliminar una parte de la lista
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
#tenemos los operadores "in" y "not in" para verificar si un elemento esta en la lista o no
my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#-------------------------------------
lista = [2, 6, 9, 15, 11, 24 , 19]
buscar = 15
encontrado = False
fin_lista = False
aux = 0

while not(encontrado) and not(fin_lista):
    if lista[aux] == buscar:
        encontrado = True
    elif aux == len(lista) - 1:
        fin_lista = True
    aux += 1
if encontrado:
    print("El elemento esta en la posicion: ", aux)
else:
    print("El elemento no esta en la lista.")
#------------------------------------------------------


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)
 

