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