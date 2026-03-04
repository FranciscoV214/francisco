def generador_numeros(limite):
    num=1
    while (num<limite):
        yield num #luego de este yield, el generador retorna un valor y la función se pausa, en el siguiente llamado (usando el método next)
        #la iteración continuará siguiendo la instrucción por debajo del yield.
        num=num + 1
numeros = generador_numeros(10) #Al haber llamado al generador, numeros se vuelve un objeto generador
print (next(numeros)) #Se aplica el metodo next aprovechando que numeros es un objeto generador
print (next(numeros))
print (next(numeros))
print (next(numeros))
print (next(numeros))