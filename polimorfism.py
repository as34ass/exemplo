class coche:
    def velocidad (self, velocidad):
    self.velocidad= velocidad
        return 'velocidad moderada'

class coche_carrera(coche):
    def velocidad_carrera (self):   
        return 'la velocidad es 200'

class coche_familiar(coche):
    def velocidad_familiar(self):
        return 'la velocidad es 150'


coche_carrera= coche_carrera()
coche

print ()

