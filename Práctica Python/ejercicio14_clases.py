class auto():
    largochasis=250
    anchochasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True

    def apagar(self):
        self.enmarcha=False
        

Miauto=auto() #instanciamos una clase, es decir creamos un objeto de la clase auto.
Miauto.arrancar()
if Miauto.enmarcha:
    print("El vehículo arrancó capo ;)")
Miauto.apagar()
if Miauto.enmarcha==False:
    print("che sabes que tuvo un problema con la junta del piston, te va a salir re caro compa...")