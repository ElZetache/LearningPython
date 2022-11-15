
#! El diccionario es otro tipo de estructura de python
#! no tiene una estructura secuencial pero se puede adaptar facilmente a ella
#! los datos van por pares que se relacionan entre ellos (key y value)
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#! podemos buscar el value de un campo en concreto buscando por la key:
print(dictionary['gato'])
print(phone_numbers['Suzy'])
#! para evitar errores al buscar una key podemos usar "in" o "not in"
dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

#! los diccionarios no se pueden recorrer por defecto con un for pero hay metodos para usar
#! una funcion intermedia para podelor hacer, por ejemplo con la funcion keyy()

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])

#! otra forma es con items()
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)

#! en los diccionarios podemos modificar el valor de las claves de la siguiente manera:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)

#! tambien se puede añadir elementos a un diccionario para esto solo hay que darle valor a una 
#! clave que no exista en el 

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)

#! y para borrar podemos usar del

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)

#! pop item es un metodo que elimina el ultima elemento del diccionario
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}

school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)