my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
fin_lista = False
i = 1

my_list.sort()
while not(fin_lista):
    if my_list[i] == my_list[i-1]:
        del my_list[i]
    else:
        i += 1
    if i == len(my_list):
        fin_lista = True


print("La lista con elementos únicos:")
print(my_list)



