
#! si queremos definir una variable dentro de una funcion y que esta sea utilizable fuera de ell
#! la declararemos como "global"

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


my_function()
print(var)
