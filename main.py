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

while run: 
    screen.fill((255, 255, 255))
    for element in elements:
        draw.rect(screen, "turquoise2", element)
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
quit()











