from random import randint
from math import hypot

def distance (pos1, pos2):
    return hypot(pos1["x"] - pos2["x"], pos1["y"] - pos2["y"])

def random(min_value, max_value, pos={"x": 0, "y": 0}, can_be_near=True):
    return_value = {"x": randint(min_value["x"], max_value["x"]), "y": randint(min_value["y"], max_value["y"])}
    if can_be_near:
        return return_value
    while distance(return_value, pos) < 25:
        return_value = {"x": randint(min_value["x"], max_value["x"]), "y": randint(min_value["y"], max_value["y"])}
    return return_value
