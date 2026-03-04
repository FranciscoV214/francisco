#Crea un programa que pida dos números por teclado. El programa tendrá una función 
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos 
#introducidos.

def DevuelveMax(numero1, numero2):
    maximo= numero1 #por defecto considero que el primer número es el mayor.
    if (numero2>numero1):
        maximo= numero2
    return maximo

num1= int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))
max=DevuelveMax(num1, num2)
print ("El máximo número introducido entre los dos es:", max)