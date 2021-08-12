contador_letras = lambda lista: [len(x) for x in lista]

lista = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista))

soma = lambda a,b: a+b
print(soma(1,1))

calculadora = {
    'soma': lambda a,b:a+b,
    'sub': lambda a,b: a-b,
    'mul': lambda a,b: a*b,
    'div': lambda a,b: a/b
}

soma = calculadora['soma']
sub = calculadora['sub']
div = calculadora['div']
mul = calculadora['mul']

print("soma: {}".format(soma(10,5)))
print("subtracao: {}".format(sub(10,5)))
print("divisao: {}".format(div(10,5)))
print("multiplicacao: {}".format(mul(10,5)))