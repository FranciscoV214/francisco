#Crea un programa que pida tres números por teclado. El programa imprime en consola 
#la media aritmética de los números introducidos.

def MediaAritmetica(lista):
    suma=lista[0]+lista[1]+lista[2]
    media=suma/3
    return media


lista_numeros=[] #inicializo una lista vacía, luego le voy agregando los números.
lista_numeros.append(int(input("Ingrese el primer número: ")))
lista_numeros.append(int(input("Ingrese el segundo número: ")))
lista_numeros.append(int(input("Ingrese el tercer número: ")))
print(MediaAritmetica(lista_numeros))