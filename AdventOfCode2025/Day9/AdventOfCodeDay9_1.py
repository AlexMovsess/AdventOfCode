import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay9.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    coordinates = [[int(x) for x in line.split(",")] for line in lines]


def calculateArea(coordinates1, coordinates2):
    area = (abs(coordinates1[0] - coordinates2[0]) + 1) * (
        abs(coordinates1[1] - coordinates2[1]) + 1
    )
    return area


maximum_area = 0

for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        maximum_area = max(maximum_area, calculateArea(coordinates[i], coordinates[j]))

print(maximum_area)
