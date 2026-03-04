#Crea un programa que pida números infinitamente. Los números introducidos deben 
#ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
#el anterior. 

flag = 0
numeros=[]
i=0
while True:
    numeros.append(int(input("Introduce un numero: ")))
    if (numeros[i]<numeros[i-1]) and flag==1:
        break
    flag = 1
    i=i+1
    
print("El número introducido es menor que el anterior. Finalizando programa...")