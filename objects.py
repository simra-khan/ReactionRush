from pygame import *

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

class Element: 
    def __init__(self, name, sprite):
        self.name = name
        self.sprite = sprite
        #self.img = transform.scale(image.load(img), (125, 125))
        #self.mask = mask.from_surface(self.img)
        #self.rect = self.mask.get_rect()

class Compound:
    def __init__(self, name, combos): #sprite, combos):
        self.name = name
        #self.sprite = transform.scale(image.load(img), (125, 125))
        self.combos = combos

class Customers:
    def __init__(self, name, sprite, order):
        self.name = name
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