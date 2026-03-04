
#Crea un programa que pida números positivos indefinidamente. El programa termina 
#cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
#todos los números introducidos.


flag = 0
numeros=[]
i=0
while True:
    valor = int(input("Introduce un numero: "))
    if (valor>0):
        numeros.append(valor)
    else:
        print("El número introducido es negativo. Finalizando programa...")
        print("La suma de los elementos introducidos es: ", sum(numeros))    
        break
    i=i+1
