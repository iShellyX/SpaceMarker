from tkinter import simpledialog
import pygame
pygame.init()

tamanho = (1000,563)
branco = (255,255,255)
icone = pygame.image.load('space.png')
fundo = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Monospace", 15, True, True)
texto = 0
coordenada = 0
cadela = False


running = True
pygame.display.set_caption('Space Marker')
tela = pygame.display.set_mode(tamanho)
pygame.display.set_icon(icone)
pygame.mixer.music.load('Space_Machine_Power.mp3')
pygame.mixer.music.play(-1)


while running:
    if cadela == True:
        arquivo = open('nome.txt', 'r')
        arquivo = arquivo.readlines(1)
        arquivo = "".join(arquivo)
        posicao = open('nome.txt', 'r')
        posicao = posicao.readlines(2)
        posicao = "".join(posicao)
        coordenada = int(posicao)
        if coordenada > 0:
            coordenada = tuple(coordenada)
            texto = font.render(arquivo + posicao, False, (255, 255, 255))
            tela.blit(texto, coordenada)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring('Space', 'Nome da estrela: ')
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
            cadela = True
            
            if item != None:
                pos1 = item + "\n" + str(pos)
                arquivo = open('nome.txt', 'a+')
                arquivo.write(pos1 + '\n')
                arquivo.close()

                pygame.draw.circle(fundo, branco, pos, 5)
                
            elif item == None:
                item = 'Desconhecido' + str(pos)
            
            
            #estrelas[item] = pos
    
    tela.fill(branco)
    tela.blit( fundo, (0,0) )
     
    
    
    pygame.display.update()
    clock.tick(40)

pygame.quit()