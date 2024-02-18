from pygame import *

class Element: 
    def __init__(self, name, img, x, y):
        self.name = name
        self.img = img
        self.sprite = transform.scale(image.load(img), (50, 50))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()
        self.x = x
        self.y = y

class Cauldron: 
    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y
        self.sprite = transform.scale(image.load(img), (200, 200))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()

class Fire:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x 
        self.y = y 
        self.sprite = transform.scale(image.load(img), (100, 100))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()

class Trash:
    def __init__(self, img, x, y):
        self.img = img
        self.x = x 
        self.y = y 
        self.sprite = transform.scale(image.load(img), (50, 50))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()

class Recipe:
    def __init__(self, img, x, y, szx, szy):
        self.img = img
        self.x = x 
        self.y = y 
        self.sprite = transform.scale(image.load(img), (szx, szy))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()



class Mouse:
    def __init__(self):
        self.surf = Surface((1, 1)).convert_alpha()
        self.surf.fill((0, 0, 0, 0))
        draw.rect(self.surf, "#FFFFFF", Rect(0, 0, 1, 1))
        self.mask = mask.from_surface(self.surf)
        self.rect = self.mask.get_rect()

class Compound:
    def __init__(self, img, name, combos, x, y): #sprite, combos):
        self.img = img
        self.name = name
        self.combos = combos
        self.x = x
        self.y = y
        self.sprite = transform.scale(image.load(img), (50, 50))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()

class Slot:
    def __init__(self, img, compound, x, y):
        self.img = img
        if (compound != None): 
            compound.sprite = transform.scale(image.load(compound.img), (50, 50))
        self.compound = compound
        self.x = x
        self.y = y
        self.sprite = transform.scale(image.load(img), (50, 50))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()

    def updateCompound(self, compound):
        if (compound != None): 
            compound.sprite = transform.scale(image.load(compound.img), (35, 35))
        self.compound = compound

class Customer:
    def __init__(self, img, order, x, y):
        self.sprite = transform.scale(image.load(img), (150, 300))
        self.order = order
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()
        self.x = x
        self.y = y
        self.timer = 45
        self.count = 0
    
    def updateTimer(self):
        self.count += 1
        if self.count == 60:
            self.count = 0
            self.timer -= 1

# class Compound: # name and sprite
#     def __init__(self, hydrogen, oxygen, carbon, nitrogen, silicon, fluorine, sodium, chlorine):
#         self.hydrogen = hydrogen
#         self.oxygen = oxygen
#         self.carbon = carbon
#         self.nitrogen = nitrogen
#         self.silicon = carbon
#         self.fluorine = fluorine
#         self.sodium = sodium
#         self.chlorine = chlorine
# # water
# if(hydrogen == 1 && oxygen == 1 ..) Compound = H2O