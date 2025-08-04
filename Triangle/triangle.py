def istriangle(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        return sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]
    return False
    
def equilateral(sides):
    if istriangle(sides): 
        return sides[0] == sides[1] == sides[2]
    return False


def isosceles(sides):
    if istriangle(sides):
        return sides[0] == sides [1] or sides[1] == sides[2] or sides[0] == sides[2]
    return False


def scalene(sides):
    if istriangle(sides):
        return equilateral == False and isosceles == False
    return False



print(isosceles([1, 3, 1]))