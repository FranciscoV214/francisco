#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos 
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por 
#teclado).

nombre = input("Ingrese su nombre: ") 
direccion = input("Ingrese su dirección: ")
tfno = int(input("Ingrese su teléfono: "))
datos_personales = [nombre, direccion, tfno]
print("Los datos personales son:", datos_personales)