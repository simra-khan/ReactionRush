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
elements.append(Element("hydrogen", "./images/elements/hydrogen.png", 100, 100))
elements.append(Element("oxygen", "./images/elements/oxygen.png", 100, 150))
elements.append(Element("carbon", "./images/elements/carbon.png", 100, 200))
elements.append(Element("nitrogen", "./images/elements/nitrogen.png", 100, 250))
elements.append(Element("silicon", "./images/elements/silicon.png", 100, 300))
elements.append(Element("fluorine", "./images/elements/fluorine.png", 100, 350))
elements.append(Element("sodium", "./images/elements/sodium.png", 100, 400))
elements.append(Element("chlorine", "./images/elements/chlorine.png", 100, 450))
compounds = mincy()

currently_dragging_object = None
dragging = False

# Cauldron variables
cauldron = Cauldron("./images/cauldron.png", width / 2 - 100, height - 600)
elements_in_cauldron = []

# Fire variables
fire = Fire("./images/fire.png", 700, 600)

# Compound output
output_compound = None
output_x = 500
output_y = 500

#inventory
inventory_list = []

#customerlist
customer_list = [0, 0, 0]
timer = 0

state = 2
mouseplace = Mouse()

game_state = 0

while run: 
    mx, my = mouse.get_pos()
    #rendering
    if game_state == 0:
        screen.fill((255, 255, 255))
        screen.blit(cauldron.sprite, (cauldron.x, cauldron.y))
        screen.blit(fire.sprite, (fire.x, fire.y))
        for i in range(len(elements)): 
            screen.blit(elements[i].sprite, (elements[i].x, elements[i].y))
        for e in elements_in_cauldron:
            screen.blit(e.sprite, (e.x, e.y))
            #draw.rect(screen, "turquoise", e.sprite) # rect->img
        if currently_dragging_object != None: 
            screen.blit(currently_dragging_object.sprite, (currently_dragging_object.x, currently_dragging_object.y))
            # draw.rect(screen, "turquoise", currently_dragging_object.sprite) # rect->img
        if output_compound != None:
            screen.blit(output_compound.sprite, (output_x, output_y))
            # draw.rect(screen, "red", output_compound.sprite) # rect->img
        
        # events
        
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN: 
                if e.button == 1:
                    # Drag into cauldron
                    for idx, element in enumerate(elements):
                        if mousecollide(element, mouseplace, mx, my):
                            currently_dragging_object = Element(element.name, element.img, mx - 25, my - 25)
                            dragging = True
                    
                    # Mix elements
                    if mousecollide(fire, mouseplace, mx, my):
                            if(output_compound == None and mix(elements_in_cauldron) != 0): 
                                output_compound = mix(elements_in_cauldron)
                                print("oh no! not a real compound")
                                elements_in_cauldron = []

                    # Move cauldron to inventory 
                    if output_compound != None and mousecollide(output_compound, mouseplace, mx, my): 
                        inventory_list.append(output_compound)
                        output_compound = None
                            
            if e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    # Drag into cauldron
                    if dragging == True: 
                        if spritecollide(cauldron, currently_dragging_object): #if (cauldron.contains(currently_dragging_object.sprite)):
                            elements_in_cauldron.append(Element(currently_dragging_object.name, currently_dragging_object.img, currently_dragging_object.x, currently_dragging_object.y))
                        currently_dragging_object = None
                        dragging = False

            if e.type == MOUSEMOTION:
                # Drag elements into cauldron
                if dragging == True:
                    currently_dragging_object.x = mx - 25
                    currently_dragging_object.y = my - 25
                
            if e.type == QUIT:
                run = False

        #customer generation
        if customer_list[0] == 0 or customer_list[1] == 0 or customer_list[2] == 0:
            timer += 1
        if timer == 600:
            emptyi = 0
            for i in range(3):
                if customer_list[i] == 0:
                    emptyi = i
            customer_list[emptyi] = Customer("./images/elements/carbon.png", random.choice(compounds))
            timer = 0
        
        for i in range(len(customer_list)):
            if (customer_list[i] != 0):
                screen.blit(customer_list[i].sprite, (100, 200))
                
    if (game_state == 1):
        startScreen(screen, width, height, font)
                     
    display.update()
    clock.tick(60)
quit()