#representamos un ajedrez con una array de 2 dimensiones (lista)
#Creamos una array de 8*8
board = []
EMPTY = ""
 
for i in range(8):
    row = [EMPTY for i in range(8)] 
    board.append(row)

#la creacion de la lista anterior se puede anidar y comprimir de la siguiente manera:
board = [[EMPTY for i in range(8)] for j in range(8)]


temperaturas = [[0.0 for hora in range(24)] for dia in range(31)]


total = 0.0
 
for day in temperaturas: #aqui a day se le asigna la array de primer nivel
    total += day[11] #aqui como tenemos la array de primer nivel solo tenemos que buscar la hora que nos
                     #interesa para hacer la media
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)

#en cambio para buscar la temperatura mas alta de todo el mes necesitariamos dos for
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]
 
print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'


var = 1
while var < 10:
    print("#")
    var = var << 1 #! repasar esto

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

my_list = [i for i in range(-1, 2)]
print(len(my_list))

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)