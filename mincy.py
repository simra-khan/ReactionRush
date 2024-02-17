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
    compounds = [Compound("water", water), Compound("methane", methane), Compound("propane", propane), Compound("glucose", glucose), Compound("acetone", acetone), Compound("alcohol", alcohol), Compound("vinegar", vinegar), Compound("caffeine", caffeine), Compound("ammonia", ammonia), Compound("glass", glass), Compound("toothpaste", toothpaste), Compound("table_salt", table_salt), Compound("bleach", bleach)]
    return compounds