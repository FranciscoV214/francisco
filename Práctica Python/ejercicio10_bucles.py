#Crea un programa que pida por teclado introducir una contraseña. La contraseña no 
#podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, 
#el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña 
#errónea” 

contrasena= input("Introduce una contraseña, deberá cumplir: \n -Tener más de 8 caracteres \n -No contar con espacios en blanco \n ")

validez=False
if (len(contrasena)>=8) and contrasena.count(" ")==0:
    validez = True

if validez:
    print("Contraseña OK")
else:
    print("Contraseña Errónea")