
#! las tuplas son parecidas a las listas con la diferencia de que no pueden variar
#! al crearlas la unica diferencia es que las listas se hacen con corchetes y las
#! tuplas con parentesis

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
print(tuple_1)
print(tuple_2)

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

