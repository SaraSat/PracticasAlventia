
class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura
    
    def area(self):
        return self.base*self.altura
    
    def perimetro(self):
        return (2 * self.base) + (2* self.altura)

class Cuadrado(Rectangulo):
    def __init__(self,lado):
        super().__init__(lado, lado)