class automovil():
        
    def __init__(self):
        self.__ruedas=4
        self.__ancho=150
        self.__largo=250
        self.__enmarcha=True

    def informacion(self):
        chequeo = self.__chequeo_interno()
        if chequeo == True and self.__enmarcha==True:
            print("El vehículo se encuentra en condiciones y puede arrancar.")
            print("El vehículo tiene las siguientes características:", self.__ruedas, "ruedas,", self.__ancho, "cm de ancho en el chasis,", self.__largo, "cm de largo en el chasis." )
        elif self.__enmarcha==False and chequeo==True:
            print("El coche está detenido, pero el chequeo es correcto.")
        else:
            print("Algo ha salido mal, el vehículo no puede arrancar...")

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite = "ok"
        self.puertas_abiertas = False
        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas_abiertas==False:
            return True
        else:
            return False
    

Miauto=automovil() #Acá se instancia la clase
Miauto.informacion()
Miauto.__chequeo_interno