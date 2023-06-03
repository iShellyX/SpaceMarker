from tkinter import simpledialog
import pygame 

from arquivo import ler_arquivo, linha, circulo, ler_linha_arquivo
pygame.init()
pygame.font.init()

tamanho = (1000,563)
branco = (255,255,255)
icone = pygame.image.load('space.png')
fundo = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
fonte = pygame.font.get_default_font() 
fontesys = pygame.font.SysFont(fonte, 20)
running = True
tela = pygame.display.set_mode(tamanho)
pontos = 0
primeira1 = 0
segunda1 = 1
primeira2 = 1
segunda2 = 3
variavel = True
condição = ler_linha_arquivo("nome.txt", primeira1)

if condição != None:
    true = True
    while true:
        linhadoarquivo = ler_linha_arquivo("nome.txt", primeira1)
        primeira1 = primeira1 +1
        segunda1 = segunda1 +1
        primeira2 = primeira2 +1
        segunda2 = segunda2 +1
        if linhadoarquivo == None:
            primeira1 = primeira1 -1
            segunda1 = segunda1 -1
            primeira2 = primeira2 -1
            segunda2 = segunda2 -1
            true = False


pygame.display.set_caption('Space Marker')
pygame.display.set_icon(icone)
pygame.mixer.music.load('Space_Machine_Power.mp3')
pygame.mixer.music.play(-1)

font = pygame.font.Font(None, 30)

tela.fill(branco)
tela.blit( fundo, (0,0) )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
            ler_arquivo("nome.txt")


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            true = True
            if pontos == 0:

                primeira1 = 0
                segunda1 = 1
                primeira2 = 1
                segunda2 = 3
                while true:
                    try:
                        circulo(tela, branco, segunda1, primeira1)
                        linha(tela, branco, primeira2, segunda2)
                        primeira1 = primeira1 +2
                        segunda1 = segunda1 +2
                        primeira2 = primeira2 +2
                        segunda2 = segunda2 +2
                        pontos = pontos +1
                    except:
                        primeira1 = primeira1 +2
                        segunda1 = segunda1 +2
                        true = False
            
            elif variavel == True:
                primeira1 = 0
                segunda1 = 1
                primeira2 = 1
                segunda2 = 3
                while true:
                    try:
                        circulo(tela, branco, segunda1, primeira1)
                        linha(tela, branco, primeira2, segunda2)
                        primeira1 = primeira1 +2
                        segunda1 = segunda1 +2
                        primeira2 = primeira2 +2
                        segunda2 = segunda2 +2
                        pontos = pontos +1
                    except:
                        primeira1 = primeira1 +2
                        segunda1 = segunda1 +2
                        true = False
                variavel = False
            
        

        elif event.type == pygame.MOUSEBUTTONUP:

            try:
                pos = pygame.mouse.get_pos()
                item = simpledialog.askstring('Space', 'Nome da estrela: ')
                if item != '':
                    nome = item
                    arquivo = open('nome.txt', 'a+')
                    arquivo.write(item + '\n' + str(pos) + '\n')
                    arquivo.close()
                    circulo(tela, branco, segunda1, primeira1)
                    primeira1 = primeira1 +2
                    segunda1 = segunda1 +2
                    pontos = pontos +1
                    
                    

                    
                else:
                    arquivo = open('nome.txt', 'a+')
                    arquivo.write("Desconhecido" + '\n' + str(pos) + '\n')
                    arquivo.close()
                    circulo(tela, branco, segunda1, primeira1)
                    primeira1 = primeira1 +2
                    segunda1 = segunda1 +2
                    pontos = pontos +1

                if pontos >= 2:
                    linha(tela, branco, primeira2, segunda2)
                    primeira2 = primeira2 +2
                    segunda2 = segunda2 +2
                    

            except:
                '''nada'''

    texto = font.render("Pressione F1 para carregar pontos"  , True, branco)

    textoDois = font.render("Pressione F2 para apagar os pontos", True, branco)

    textoTres = font.render("Pressione F3 para salvar os pontos", True, branco)

    tela.blit( texto, (10, 10) )
    tela.blit( textoDois, (10, 35) )
    tela.blit(textoTres, (10, 60))
    
    pygame.display.update()
    clock.tick(40)

pygame.quit()