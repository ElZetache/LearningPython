#Python language
def tabla(tab):      
    print (f'Tabla del', tab)
    for factor in range(11):
        print (f'{tab} x {factor} = {tab * factor}')
    print("\n")

def escoger_tablas():
    lista_tablas = []
    tabla = "0"
    while tabla != "":
        try:
            tabla = (input("Introduce una tabla: (cuando no quieras mas tablas pulsa enter): "))
            lista_tablas.append(int(tabla))
        except:
            if tabla != "":
                print("El valor introducido no es valido")
    return lista_tablas


tablas = escoger_tablas()
for tab in tablas:
    tabla(tab)


    