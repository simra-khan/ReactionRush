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
            return c
    return 0

def mousecollide(object, mouse, mx, my):
    if object.mask.overlap(mouse.mask, (mx - object.x, my - object.y)):
        return True
    else:
        return False

def spritecollide(object1, object2):
    ov = object1.mask.overlap_area(object2.mask, (object2.x - object1.x, object2.y - object1.y))
    if ov == object2.mask.count():
        return True
    else:
        return False