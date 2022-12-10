def smash(words):
    frase = " ".join(words)
    return frase

def basic_op(operator, value1, value2):

   
    if (operator == "+"): res = value1 + value2
    elif (operator == "-"): res = value1 - value2
    elif (operator == "*"): res = value1 * value2 
    elif (operator == "/"): res = value1 / value2


    return res

def count_positives_sum_negatives(arr):
    if (len(arr) == 0):
        lista = []
    else:
        lista = [0,0]
    for num in arr:
        if(num<=0): lista[1] = lista[1] + num
        else: lista[0] = lista[0] + 1
    return lista

def century(year):
    century = 0
    if((year/100)>(int(year/100))): century = int(year/100) + 1
    else: century = int(year/100)
    return century