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



def linha(tela, branco, primeira2, segunda2):
    coordenadax = ""
    coordenaday = ""
    pontolinha1 = ler_linha_arquivo("nome.txt", primeira2)

    for i in pontolinha1:
        if i == "(" or i == ")" or i == "\n" or i == " ":
            i = ""
        elif i == ",":
            break
        coordenadax = coordenadax + i
    coordenadax = int(coordenadax)
    for i in pontolinha1:
        if i == "(" or i == ")" or i == "\n" or i == " ":
            i = ""
        elif i == ",":
            coordenaday = ""
            i = ""
            
        coordenaday = coordenaday + i
    coordenaday = int(coordenaday)
    ponto1 = (coordenadax, coordenaday)


    coordenadax = ""
    coordenaday = ""
    pontolinha2 = ler_linha_arquivo("nome.txt", segunda2)
    for i in pontolinha2:
        if i == "(" or i == ")" or i == "\n" or i == " ":
            i = ""
        elif i == ",":
            break
        coordenadax = coordenadax + i
    coordenadax = int(coordenadax)
    for i in pontolinha2:
        if i == "(" or i == ")" or i == "\n" or i == " ":
            i = ""
        elif i == ",":
            coordenaday = ""
            i = ""
            
        coordenaday = coordenaday + i
    coordenaday = int(coordenaday)
    ponto2 = (coordenadax, coordenaday)
        
    pygame.draw.line(tela, branco, (ponto1), (ponto2), 1)




def circulo(tela, branco, segunda1, primeira1):
    coordenadax = ""
    coordenaday = ''
    texto1 = ler_linha_arquivo("nome.txt", (primeira1))
    pontocirculo = ler_linha_arquivo("nome.txt", segunda1)


    for i in pontocirculo:
        if i == "(" or i == ")" or i == "\n" or i == " ":
            i = ""
        elif i == ",":
            break
        coordenadax = coordenadax + i
    coordenadax = int(coordenadax)

    for i in pontocirculo:
        if i == "(" or i == ")" or i == "\n" or i == " ":
            i = ""
        elif i == ",":
            coordenaday = ""
            i = ""
    
            
        coordenaday = coordenaday + i
    coordenaday = int(coordenaday)
    
    circulo = (coordenadax, coordenaday)
    texto1 = texto1 + pontocirculo
    fonte = pygame.font.get_default_font() 
    fontesys = pygame.font.SysFont(fonte, 20)
    texto = fontesys.render(texto1, 1, branco)
    
    tela.blit(texto, circulo)
    pygame.draw.circle(tela, branco, circulo, 5)