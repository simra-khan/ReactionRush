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

currently_dragging_element = None
dragging_element = False

# Cauldron variables
cauldron = Cauldron("./images/cauldron.png", width / 2 - 100, height - 500)
elements_in_cauldron = []

# Fire variables
fire = Fire("./images/fire.png", 700, 660)

#Trash
trash = Trash("./images/fire.png", 900, 400)

# Compound output
output_compound = None
output_x = 900
output_y = 450

#inventory
inventory_list = []

#customerlist
customer_images = ["./images/girl.png", "./images/guy.png"]
customer_list = [None, None, None]
timer = 0

#slots
slots = []
for i in range(8):
    slots.append(Slot("./images/slot.png", None, 50 * i, 800))
currently_dragging_slot = None
dragging_slot = False
slot_index = 0

mouseplace = Mouse()

game_state = 1

while run: 
    mx, my = mouse.get_pos()
    #rendering
    if game_state == 0:
        screen.fill((255, 255, 255))
        screen.blit(cauldron.sprite, (cauldron.x, cauldron.y))
        screen.blit(fire.sprite, (fire.x, fire.y))
        screen.blit(trash.sprite, (trash.x, trash.y))
        for i in range(len(elements)): 
            screen.blit(elements[i].sprite, (elements[i].x, elements[i].y))
        for e in elements_in_cauldron:
            screen.blit(e.sprite, (e.x, e.y))
        if output_compound != None:
            screen.blit(output_compound.sprite, (output_compound.x, output_compound.y))
        for i in slots:
            screen.blit(i.sprite, (i.x, i.y))
            if i.compound != None:
                screen.blit(i.compound.sprite, (i.x + 5, i.y + 5))
        if currently_dragging_element != None: 
            screen.blit(currently_dragging_element.sprite, (currently_dragging_element.x, currently_dragging_element.y))
        if currently_dragging_slot != None:
            screen.blit(currently_dragging_slot.sprite, (currently_dragging_slot.x, currently_dragging_slot.y))
        

        

        # events
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN: 
                if e.button == 1:
                    print(currently_dragging_slot)
                    # Drag into cauldron
                    for idx, element in enumerate(elements):
                        if mousecollide(element, mouseplace, mx, my) and not dragging_element and not dragging_slot:
                            currently_dragging_element = Element(element.name, element.img, mx - 25, my - 25)
                            dragging_element = True
                     
                    # Drag to customer
                    for idx, slot in enumerate(slots):
                        if mousecollide(slot, mouseplace, mx, my) and not dragging_element and not dragging_slot and slot.compound != None:
                            currently_dragging_slot = slot.compound
                            currently_dragging_slot.x = mx - 20
                            currently_dragging_slot.y = my - 20
                            dragging_slot = True
                            slot_index = idx
                    
                    # Mix elements
                    if mousecollide(fire, mouseplace, mx, my):
                        if(output_compound == None and mix(elements_in_cauldron) != 0): 
                            output_compound = mix(elements_in_cauldron)
                            elements_in_cauldron = []

                    # Trash elements
                    if mousecollide(trash, mouseplace, mx, my):
                        elements_in_cauldron = []

                    # Move output to inventory 
                    if output_compound != None and mousecollide(output_compound, mouseplace, mx, my): 
                        for i in slots:
                            if i.compound == None:
                                i.updateCompound(output_compound)
                                output_compound = None
                                break
                        
            if e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    # Drag into cauldron
                    if dragging_element == True: 
                        if spritecollide(cauldron, currently_dragging_element): 
                            elements_in_cauldron.append(Element(currently_dragging_element.name, currently_dragging_element.img, currently_dragging_element.x, currently_dragging_element.y))
                        currently_dragging_element = None
                        dragging_element = False
                    
                    # Drag to customer
                    if dragging_slot == True: 
                        for i in range(len(customer_list)):
                            cur = customer_list[i]
                            if spritecollideunfull(cur, currently_dragging_slot):
                                if (cur.order.name == currently_dragging_slot.name):
                                    customer_list[i] = None
                                    slots[slot_index].updateCompound(None)
                                    break
                        currently_dragging_slot = None
                        dragging_slot = False

            if e.type == MOUSEMOTION:
                # Drag elements into cauldron
                if dragging_element == True:
                    currently_dragging_element.x = mx - 25
                    currently_dragging_element.y = my - 25
                if dragging_slot == True:
                    currently_dragging_slot.x = mx - 25
                    currently_dragging_slot.y = my - 25
                
            if e.type == QUIT:
                run = False

        #customer generation
        if customer_list[0] == None or customer_list[1] == None or customer_list[2] == None:
            timer += 1
        if timer == 200:
            emptyi = 0
            for i in range(3):
                if customer_list[i] == None:
                    emptyi = i
                    customer_list[emptyi] = Customer(random.choice(customer_images), random.choice(compounds), 500 + i * 100, 400)#random.choice(compounds))
                    break
            timer = 0
        
        for i in range(len(customer_list)):
            if (customer_list[i] != None):
                screen.blit(customer_list[i].sprite, (customer_list[i].x, customer_list[i].y))
                screen.blit(customer_list[i].order.sprite, (customer_list[i].x, customer_list[i].y - 100))
                
    if (game_state == 1):
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                game_state = 0
            if e.type == KEYDOWN:
                game_state = 0
        startScreen(screen, width, height, my_font)
                     
    display.update()
    clock.tick(60)
quit()