#Create a Python function that takes a sequence of 
#comma-separated numbers as input and generates both a 
#list and a tuple containing those numbers.

def string_a_cadena_y_tupla(cadena):
    valores_lista=cadena.split(",") #Esta linea genera una lista, donde cada elemento es una subcadena obtenida al separar
    return valores_lista, tuple(valores_lista)

lista, tupla = string_a_cadena_y_tupla(str(input("Introduce una cadena de números separados por ','")))
print(lista)
print(tupla)

