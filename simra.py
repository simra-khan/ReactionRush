import pygame

def startScreen(screen, width, height, font):
    screen.fill((0, 0, 0))
    title = font.render('Cooking Walter White', True, (255, 255, 255))
    start_button = font.render('Press any button to start the game', True, (255, 255, 255))
    screen.blit(title, (width/2 - title.get_width()/2, height/2 - title.get_height()/2))
    screen.blit(start_button, (width/2 - start_button.get_width()/2, height/2 + start_button.get_height()/2))
    pygame.display.update()
