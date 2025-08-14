#Create a Python program that identifies all numbers between 100 and 300 (inclusive) 
#that are divisible by 7 but not multiples of 5. 
#The identified numbers should be displayed in a single line, separated by commas.

numeros = [] 
numeros_validos = []
for i in range (100, 300+1, 1):
    numeros.append(i)
    if (numeros[i-100]%7==0 and numeros[i-100]%5!=0):
        numeros_validos.append(numeros[i-100])
print("Los números entre 100 y 300 que son divisibles entre 7 y no son múltiplos de 5 son: \n", numeros_validos)