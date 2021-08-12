a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

soma = a+b
sub = a-b
div = a/b
mult = a*b
resto = a%b

resultado = (f'Soma: {soma}, diferença = {sub}, divisao = {div}, produto = {mult}, resto = {resto}'.format(soma=soma, sub = sub, div =div, produto = mult, resto = resto))
print(resultado)

