import random
from pygame import *
from objects import *
from logic import *
from mincy import *
from simra import *

init()

screen = display.set_mode()
width, height = screen.get_size()
clock = time.Clock()
font.init()
my_font = font.SysFont('Comic Sans MS', 18)

run = True

# Elements variables
elements = []
elements.append(Element("hydrogen", Rect(100, height / 2, 20, 20)))
elements.append(Element("oxygen", Rect(width - 100, height / 2, 20, 20)))
currently_dragging_object = None
dragging = False

# Cauldron variables
cauldron = Rect(width / 2 - 100, height - 500, 200, 120)
elements_in_cauldron = []
compoundslist = mincy() # do we need this? if not we can delete

# Fire variables
fire = transform.scale(image.load("./images/fire.png"), (100, 100))
fire_x = 700
fire_y = 600

# Compound output
output_compound = None

#inventory
inventory_list = []

state = 2

while run: 
    #rendering
    screen.fill((255, 255, 255))
    draw.rect(screen, "black", cauldron)
    for e in elements:
        draw.rect(screen, "turquoise", e.sprite)
    for e in elements_in_cauldron:
        draw.rect(screen, "turquoise", e.sprite)
    if(currently_dragging_object != None): 
        draw.rect(screen, "turquoise", currently_dragging_object.sprite)
    # if(output_compound != None):
    #     draw.rect(screen, output_compound.sprite, Rect(100, 100, 40, 40))
    screen.blit(fire, (fire_x, fire_y))
    
    # events
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN: 
            if e.button == 1:
                # Drag into cauldron
                for idx, element in enumerate(elements):
                    if element.sprite.collidepoint(e.pos):
                        currently_dragging_object = Element(element.name, Rect(element.sprite.x, element.sprite.y, element.sprite.w, element.sprite.h))
                        dragging = True
                # Mix elements
                if fire.get_rect(topleft=(fire_x, fire_y)).collidepoint(e.pos):
                        print(mix(elements_in_cauldron).name)
                        if(mix(elements_in_cauldron) != 0): 
                            output_compound = mix(elements_in_cauldron)
                            print("ran")
                        elements_in_cauldron = []

                # Move cauldron to inventory 
                if output_compound != None and output_compound.collidepoint(e.pos):
                    inventory_list.append(output_compound)
                    output_compound = None
                        
        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                # Drag into cauldron
                if dragging == True: 
                    if(cauldron.contains(currently_dragging_object.sprite)):
                        elements_in_cauldron.append(Element(currently_dragging_object.name, Rect(currently_dragging_object.sprite.x, currently_dragging_object.sprite.y, currently_dragging_object.sprite.w, currently_dragging_object.sprite.h)))
                    currently_dragging_object = None
                    dragging = False

        if e.type == MOUSEMOTION:
            # Drag elements into cauldron
            if dragging == True:
                currently_dragging_object.sprite.move_ip(e.rel)
            
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(60)
quit()