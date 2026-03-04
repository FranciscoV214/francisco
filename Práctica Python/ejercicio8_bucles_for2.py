while True: #acá meti un while porque me pintó, todavía no se ve en el curso jajaj
    correo = input("Introduce tu correo electronico: ")
    if "@" in correo:
        usuario, dominio = correo.split("@") #Dividi al correo en dos partes, el usuario (antes del arroba) y el dominio (despues del arroba)
        if correo.count("@")==1 and dominio.count("."): #Tiene que haber solo un arroba en el correo y un punto en el dominio.
            print("El correo electrónico es válido...")
        else:
            print("El correo electrónico introducido no es válido...")

    else:
        print("El correo electrónico introducido no es válido...")
