def ler_linha_arquivo(nome_arquivo, numero_linha):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        if numero_linha < len(linhas):
            linha_desejada = linhas[numero_linha]
            return linha_desejada
        else:
            return None

def ler_arquivo(nome_arquivo,):
    with open(nome_arquivo, 'w') as arquivo:
        linhas = arquivo.write('')
        return linhas
    
def salvar():
    arquivo = open('memoria.txt', 'r')
    arquivo = arquivo.read()
    arquivo = "".join(arquivo)
    arquivo2 = open("nome.txt", 'a+')
    arquivo2.write(arquivo)
    arquivo2.close()