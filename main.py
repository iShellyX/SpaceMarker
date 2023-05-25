from tkinter import simpledialog
import pygame 

from arquivo import ler_linha_arquivo, ler_arquivo, salvar, linha
pygame.init()
pygame.font.init()

tamanho = (1000,563)
branco = (255,255,255)
icone = pygame.image.load('space.png')
fundo = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
fonte = pygame.font.get_default_font() 
fontesys = pygame.font.SysFont(fonte, 20)
primeira = 0
segunda = 1
running = True
true = False
tela = pygame.display.set_mode(tamanho)
pontos = 0
primeira2 = 1
segunda2 = 3

pygame.display.set_caption('Space Marker')
pygame.display.set_icon(icone)
pygame.mixer.music.load('Space_Machine_Power.mp3')
pygame.mixer.music.play(-1)

tela.fill(branco)
tela.blit( fundo, (0,0) )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar()
            ler_arquivo("memoria.txt")
            running = False


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            salvar()
            ler_arquivo("memoria.txt")
            running = False


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F2:
            ler_arquivo("nome.txt")


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            true = True
            while true:
                try:
                    arquivo = ler_linha_arquivo("nome.txt", primeira)
                    arquivo = "".join(arquivo)
                    posicao = ler_linha_arquivo("nome.txt", segunda)
                    coordenada = list(posicao)
                    coordenadax = coordenada[1] + coordenada[2] + coordenada[3]
                    coordenaday = coordenada[6] + coordenada[7] + coordenada[8]
                    coordenada = (int(coordenadax), int(coordenaday))
                    texto = fontesys.render(arquivo + posicao, 1, branco)
                    tela.blit(texto, coordenada)
                    pygame.draw.circle(tela, branco, coordenada, 5)
                    primeira = primeira + 2
                    segunda = segunda + 2
                except:
                    true = False

                    
        elif event.type == pygame.MOUSEBUTTONUP:
            try:
                pos = pygame.mouse.get_pos()
                item = simpledialog.askstring('Space', 'Nome da estrela: ')
                if item != '':
                    pos1 = item + "\n" + str(pos)
                    arquivo = open('memoria.txt', 'a+')
                    arquivo.write(pos1 + '\n')
                    arquivo.close()
                    texto = fontesys.render(pos1, 1, branco)
                    tela.blit(texto, pos)
                    pygame.draw.circle(tela, branco, pos, 5)
                    pontos = pontos +1
                    if pontos >= 2:
                        linha(tela, branco, primeira2, segunda2)
                        primeira2 = primeira2 + 2
                        segunda2 = segunda2 + 2

                    
                else:
                    arquivo = open('memoria.txt', 'a+')
                    arquivo.write("Desconhecido" + '\n' + str(pos) + '\n')
                    arquivo.close()
                    texto = fontesys.render('Desconhecido'+ str(pos), 1, branco)
                    tela.blit(texto, pos)
                    pygame.draw.circle(tela, branco, pos, 5)
            except:
                '''nada'''


        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F3:
            salvar()
            ler_arquivo("memoria.txt")


    
    pygame.display.update()
    clock.tick(40)

pygame.quit()