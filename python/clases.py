# fichero clases.py

""" Este es el constructor de la clase Animal, donde self es la propia 
    instancia de la clase, el primer parámetro que recibe el método, la clase tiene dos funciones, info y mover"""
class Animal:
    def __init__(self, nombre, npatas, puedo_volar=False): 
        self.nombre=nombre
        self.npatas=npatas
        self.puedo_volar=puedo_volar
        self.x=0
        self.y=0

    def info(self):
        print('Me llamo {0},tengo {1} patas y {2}'.format(
            self.nombre, self.npatas,
            'puedo volar' if self.puedo_volar else 'No puedo volar'
        ))

    def mover(self, x, y):
        self.x, self.y = x, y
        print('Me he movido a {0},{1}'.format(x,y))

"""Clase Ave que hereda de la clase Animal, en el constructor se instancia a la clase padre mediante super, 
llamando así a su constructor"""
class Ave(Animal):
  
    def __init__(self):
        super().__init__('AVE',2,True)


class Mamifero(Animal):
    def __init__(self):
        super().__init__('MAMIFERO',4)
