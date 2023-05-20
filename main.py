from tkinter import simpledialog
import pygame
pygame.init()

tamanho = (1000,563)
branco = (255,255,255)
icone = pygame.image.load('space.png')
fundo = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()

running = True
pygame.display.set_caption('Space Marker')
tela = pygame.display.set_mode(tamanho)
pygame.display.set_icon(icone)
pygame.mixer.music.load('Space_Machine_Power.mp3')
pygame.mixer.music.play(-1)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring('Space', 'Nome da estrela: ')
            print(item)
            if item == None:
                item = 'Desconhecido' + str(pos)
            #estrelas[item] = pos
    
    tela.fill(branco)
    tela.blit( fundo, (0,0) )

    
    
    pygame.display.update()
    clock.tick(40)

pygame.quit()