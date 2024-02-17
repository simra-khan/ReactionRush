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