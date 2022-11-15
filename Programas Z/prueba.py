

def find_outlier(integers):
    esPar = False
    esImpar = False
    num = 0
    #Primero buscamos si el numero diferente es par o impar
    if integers[0] %2 == 0:
        if integers[1] %2 == 0:
            esImpar = True
        elif integers[2] %2 == 0:
            esImpar = True
        else:
            esPar = True
    elif integers[1] %2 != 0:
        print("es par")
        esPar = True
    elif integers[2] %2 == 0:
        esImpar = True
    else:
        print("entra en el else")
        esPar = True
    
    if esPar:
        for x in integers:
            if x%2 == 0:
                print(x)
                num = x
    elif esImpar:
        for x in integers:
            if x%2 != 0:
                num = x
                
    


    return num


print(find_outlier([-6992391, -9861356, -7909599, 485869, 2184793, 7022717, 4051319, -2340389, 2097427, 3596565, -1626933, 9664495, 1474973, -3112087, 9391799, 9602213, 7763441, 2592553, 3679851, 9000461, 560831, 6341537, 9104405, 1675711, 9257055, -7895983, -4230685, 767405, 3361155, 718157, 6133429, 5268079, 4641531, 7906477, -5244873, 8796333, -2155981]))
#impar, par, impar