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
        "hydrogen": 4,
        "oxygen": 2
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

    output_x = 180
    output_y = 510
    compounds = [
        Compound("./images/water.png", "water", water, output_x, output_y), 
        Compound("./images/methane.png", "methane", methane, output_x, output_y), 
        Compound("./images/propane.png", "propane", propane, output_x, output_y),
        Compound("./images/glucose.png", "glucose", glucose, output_x, output_y),
        Compound("./images/acetone.png", "acetone", acetone, output_x, output_y),
        Compound("./images/alcohol.png", "alcohol", alcohol, output_x, output_y),
        Compound("./images/vinegar.png", "vinegar", vinegar, output_x, output_y),
        Compound("./images/caffeine.png", "caffeine", caffeine, output_x, output_y),
        Compound("./images/ammonia.png", "ammonia", ammonia, output_x, output_y),
        Compound("./images/glass.png", "glass", glass, output_x, output_y),
        Compound("./images/toothpaste.png", "toothpaste", toothpaste, output_x, output_y),
        Compound("./images/salt.png", "table_salt", table_salt, output_x, output_y),
        Compound("./images/bleach.png", "bleach", bleach, output_x, output_y)
        ]
    return compounds