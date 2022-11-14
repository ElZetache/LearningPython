#metodo burbuja
lista = [8, 10, 6, 2, 4]
cambios = True

while cambios:
    cambios = False
    for x in range(len(lista)-1):
        if lista[x] > lista[x+1]:
            lista[x], lista[x+1] = lista[x+1], lista[x]
            cambios = True
print(lista)
#Esta bien estos metodos para entender los algoritmos, pero pyhton ya tiene sus propias
#funciones que nos facilitan la tarea:
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print("2:", my_list)
#reverse invierte la lista:
my_list = [8, 10, 6, 2, 4]
my_list.reverse()
print("3:", my_list)
my_list.sort()
my_list.reverse()
print("4:", my_list)
 
