lista = [1,10]
arquivo = open('teste.txt', 'r')
try:
    numero = lista[1]
    texto = arquivo.read()
    div = 10 / 1
    print('fechando arquivo')
    arquivo.close()
    # x = a
except ZeroDivisionError:
    print("Nao eh possivel realizar uma divisao por zero")
except IndexError:
    print("o programa esta tentando acessar uma posicao invalida do vetor")
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print("Nao rolou nenhum erro")
finally:
        print('sempre executa')
        arquivo.close()
