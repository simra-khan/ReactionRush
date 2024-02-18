from objects import *
from mincy import *

compounds = mincy()

def mix(cauldron):
    mp = {}
    for c in cauldron:
        mp[c.name] = 0
    for c in cauldron:
        mp[c.name] += 1
    for c in compounds:
        if mp == c.combos:
            return Compound(c.img, c.name, c.combos, c.x, c.y)
    return 0

def mousecollide(object, mouse, mx, my):
    if (object == None):
        return False
    if object.mask.overlap(mouse.mask, (mx - object.x, my - object.y)):
        return True
    else:
        return False

def spritecollide(object1, object2):
    if (object1 == None or object2 == None):
        return False
    ov = object1.mask.overlap_area(object2.mask, (object2.x - object1.x, object2.y - object1.y))
    if ov == object2.mask.count():
        return True
    else:
        return False
    
def spritecollideunfull(object1, object2):
    if (object1 == None or object2 == None):
        return False
    ov = object1.mask.overlap_area(object2.mask, (object2.x - object1.x, object2.y - object1.y))
    if ov != 0:
        return True
    else:
        return False