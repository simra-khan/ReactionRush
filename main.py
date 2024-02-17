import random
from pygame import *
from objects import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()
font.init()
my_font = font.SysFont('Comic Sans MS', 18)


run = True

elements = []
for i in range(2):
    x = random.randint(100, 800)
    y = random.randint(100, 800)
    elements.append(Rect(x, y, 50, 50))
selected_piece = None

while run: 
    screen.fill((255, 255, 255))
    for element in elements:
        draw.rect(screen, "turquoise", element)
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN: 
            if e.button == 1:
                for idx, element in enumerate(elements):
                    if element.collidepoint(e.pos):
                        selected_piece = idx
        
        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                selected_piece = None

        if e.type == MOUSEMOTION:
            if selected_piece != None:
                elements[selected_piece].move_ip(e.rel)
            
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(60)
quit()











