
#! podemos devolver datos desde las funciones con return
def boring_function():
    return 123
 
x = boring_function()
 
print("La función boring_function ha devuelto su resultado. Es:", x)

#! si una funcion de la cual se espera que devuelva un resultado no lo hace devolverá "none"
def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))

#! Tambien se le puede pasar una lista como argumento a una funcion:

def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
print(list_sum([5, 4, 3]))

#! y tambien puede devolver una lista por el return:
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
