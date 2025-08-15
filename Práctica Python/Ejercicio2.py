#Create a Python function that takes an integer (n) as input and generates a dictionary containing pairs ((i, i^2))
#for all integers (i) from 1 to (n) (inclusive). The function should then return this dictionary.

def diccionario_exponentes(n):
    diccionario = {
        "numero": [],
        "exponente": []
    }

    for i in range (1, n+1, 1):
        diccionario["numero"].append(i)
        diccionario["exponente"].append(i*i)

    print("{ ")
    for j in range (0, n, 1):
        print(diccionario["numero"][j], ":", diccionario["exponente"][j])
    print(" }")

n=int(input("Selecciona un número entero 'n': \n"))
diccionario_exponentes(n)
