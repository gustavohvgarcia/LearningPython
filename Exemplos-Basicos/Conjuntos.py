# conjunto = {1,2,3,4}
# conjunto.add(5)
# conjunto.discard(2)
#
# print(conjunto)

conjunto = {1,2,3,4}
conjunto2 = {1,2,3,4,5,6}
conjunto_uniao = conjunto.union(conjunto2)
conjunto_inter = conjunto.intersection(conjunto2)
conjunto_diferenca = conjunto2.difference(conjunto)
conjunto_diferenca2 = conjunto.difference(conjunto2)

print("Primeiro conjunto: " + str(conjunto))
print("Segundo conjunto: " + str(conjunto2))
print("Conjunto uniao: " + str(conjunto_uniao))
print("Conjunto Interseccao: " + str(conjunto_inter))
print("Conjunto diferenca: " + str(conjunto_diferenca))
print("Conjunto diferenca 2: " + str(conjunto_diferenca2))