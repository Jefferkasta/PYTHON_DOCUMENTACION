class Aritmetica:
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multi(self):
        return self.operandoA * self.operandoB
    def div(self):
        return self.operandoA / self.operandoB
aritmetica1 = Aritmetica(5,3)
print(f'la suma es: {aritmetica1.sumar()}')
print(f'la suma es: {aritmetica1.restar()}')
print(f'la suma es: {aritmetica1.multi()}')
print(f'la suma es: {aritmetica1.div()}')
        #sesion=10 video=99