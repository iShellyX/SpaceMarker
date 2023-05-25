import pygame

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

def linha(tela, branco, primeira2, segunda2):
    pontolinha1 = ler_linha_arquivo("memoria.txt", primeira2)
    coordenada1 = list(pontolinha1)
    if coordenada1[3] == ",":
        coordenada1[3] = None
    coordenadax = coordenada1[1] + coordenada1[2] + coordenada1[3]
    coordenaday = coordenada1[6] + coordenada1[7] + coordenada1[8]
    coordenada1 = (int(coordenadax), int(coordenaday))
    
    pontolinha2 = ler_linha_arquivo("memoria.txt", segunda2)
    coordenada2 = list(pontolinha2)
    if coordenada2[3] == ",":
        coordenadax = coordenada2[1] + coordenada2[2]
    else:
        coordenadax = coordenada2[1] + coordenada2[2] + coordenada2[3]
    coordenaday = coordenada2[6] + coordenada2[7] + coordenada2[8]
    coordenada2 = (int(coordenadax), int(coordenaday))
    pygame.draw.line(tela, branco, (coordenada1), (coordenada2), 1)