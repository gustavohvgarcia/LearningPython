def atualizar_arquivo(texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()


def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


# pode ser passado o diretorio do arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read()
    print(texto)
    arquivo.close()


if __name__ == '__main__':
    escrever_arquivo('Primeira linha\n')
    atualizar_arquivo('Segunda linha\n')
    atualizar_arquivo('Terceira linha\n')
    atualizar_arquivo('Quarta linha\n')
    ler_arquivo('teste.txt')
