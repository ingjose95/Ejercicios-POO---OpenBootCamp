class Vehiculo:

    color = 'rojo'
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):

    velocidad = '200 Km por hora'
    cilindrada = 4

    def descripcionCoche(self):

        print('El coche es de color', self.color, '\nTiene ', self.ruedas, 'ruedas'
        , '\nTiene', self.puertas, 'puertas', '\nSu velocidad es de', self.velocidad
        , '\nTiene', self.cilindrada, 'cilindros')

c = Coche()
c.descripcionCoche()