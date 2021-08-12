class Calculadora:

    def soma(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a/b

if __name__ == '__main__':
    calculadora = Calculadora(10,2)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.div())
    print(calculadora.mul())
