a = int(input("entre com um numero: "))

div = 0
for x in range (1,a+1):
    resto = a % x
    if resto == 0:
        div+=1

if div == 2:
    print("numero {} eh primo ".format(a))
else:
    print("numero {} nao eh primo".format(a))

