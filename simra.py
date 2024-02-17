import pygame

def startScreen():

    screen.fill((0, 0, 0))
    font = font.SysFont('arial', 40)
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (width/2 - title.get_width()/2, height/2 - title.get_height()/2))
    screen.blit(start_button, (width/2 - start_button.get_width()/2, height/2 + start_button.get_height()/2))
    pygame.display.update()
