
#! es importante controlar que los datos que nos llegan a nuestras funciones sean validos para
#! evitar fallos de ejecucion
#! en python se suele usar try: except: en vez de un if para comprobar el valor
value = input('Ingresa un número natural: ')
try:
    int_value = int(value)
    print('El recíproco de', int_value, 'es', 1/int_value)        
except ValueError:
    print('No se que hacer con', value)
#! tambien podemos poner diferentes except segun el tipo de error que arroje Phyton
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.') 
#! si ponemos un except sin especificar a que error esta relacionado este será el que saldrá por defecto
#! para los errores que no esten controlados, este siempre tiene que ser el ultimo
except:
    print("Ha ocurrido un error inesperado")

#Algunas excepciones utiles:
#   - ZeroDivisionError
#   - ValueError
#   - TypeError
#   - AtributeError
#   - SintaxError


try:
    value = input("Ingresa un valor: ")
    print(value/value)
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada errónea...")
except TypeError:
    print("Entrada muy errónea...")
except:
    print("¡Buuu!")

 
