from Televisao import Televisao
from Calculadora import Calculadora

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora()
    print(calculadora.soma(10,2))
    print(calculadora.sub(10,2))
    print(calculadora.div(10,2))
    print(calculadora.mul(10,2))