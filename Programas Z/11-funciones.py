#? usamos def para definir funciones
#Python es un lenguaje interpretado, al ser lineal las funciones se tienen que declarar antes de ser
#usadas
def message(what, number):
    print("Ingresa", what, "número", number)
 

message("telefono", 11)
message("precio", 5)
message("numero", "number")


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction2(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction2("Skywalker", "Luke")
introduction2("Quick", "Jesse")
introduction2("Kent", "Clark")

#! Tambien se pueden pasar los argumento por palabra clave, asi no afectaría el orden:
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

#! se les puede asignar un valor por defecto a los argumentos, esto se usará en caso de que no le llegue
def introduction3(first_name="Rodrigo", last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)
introduction3("Jorge", "Pérez")
introduction3("Albert")
introduction3()