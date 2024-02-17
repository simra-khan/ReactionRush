from pygame import *
from objects import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()
font.init()
my_font = font.SysFont('Comic Sans MS', 18)


run = True

while run: 
    screen.fill((255, 255, 255))
    draw.rect(screen, "#000000", Rect(100, height / 2, 50, 50))
    draw.rect(screen, "#000000", Rect(width - 100, height / 2, 50, 50))
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
quit()











