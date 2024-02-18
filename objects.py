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
        self.sprite = transform.scale(image.load(img), (200, 200))
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
        self.sprite = transform.scale(image.load(img), (125, 125))
        self.mask = mask.from_surface(self.sprite)
        self.rect = self.mask.get_rect()





class Customer:
    def __init__(self, sprite, order):
        self.sprite = sprite
        self.img = transform.scale(image.load(sprite), (125, 125))
        self.order = order

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