from objects import *

def mincy():
    water = {
        "hydrogen": 2,
        "oxygen": 1
    }
    methane = {
        "carbon": 1,
        "hydrogen": 4
        }
    propane = {
        "carbon": 3,
        "hydrogen": 8
        }
    glucose = {
        "carbon": 6,
        "hydrogen": 12,
        "oxygen":6
        }
    acetone = {
        "carbon": 3,
        "hydrogen": 6,
        "oxygen":1
        }
    alcohol = {
        "carbon": 2,
        "hydrogen": 6,
        "oxygen": 1
        }
    vinegar = {
        "carbon": 2,
        "hydrogen": 6,
        "oxygen": 1
        }
    caffeine = {
        "carbon": 8,
        "hydrogen": 10,
        "nitrogen": 4,
        "oxygen": 1
        }
    ammonia = {
        "nitrogen": 1,
        "hydrogen": 3
    }
    glass = {
        "silicon": 1,
        "oxygen": 2
    }
    toothpaste = {
        "sodium": 1,
        "fluorine": 1
    }
    table_salt = {
        "sodium": 1,
        "chlorine": 1
    }
    bleach = {
        "sodium": 1,
        "chlorine": 1,
        "oxygen": 1
    }

    compounds = [Compound("./images/water.png", "water", water, 0, 0)] #, Compound("methane", methane, "orange"), Compound("propane", propane, "yellow"), Compound("glucose", glucose, "lime"), Compound("acetone", acetone, "green"), Compound("alcohol", alcohol, "aqua"), Compound("vinegar", vinegar, "blue"), Compound("caffeine", caffeine, "purple"), Compound("ammonia", ammonia, "magenta"), Compound("glass", glass, "pink"), Compound("toothpaste", toothpaste, "brown"), Compound("table_salt", table_salt, "grey"), Compound("bleach", bleach, "black")
    return compounds