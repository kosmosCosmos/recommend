import math

a = ["a", "b", "c"]
b = ["a", "c", "d"]
c = ["b", "d", "e"]
d = ["a", "f"]


def similar(group1, group2):
    i = 0
    for x in group1:
        for y in group2:
            if x == y:
                i = i + 1
    if i == 0:
        print(0)
    else:
        print(i / math.sqrt(len(group1) * len(group2)))

similar(c, d)
