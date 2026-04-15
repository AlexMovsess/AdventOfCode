import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay1.txt")) as f:
    lines = f.readlines()

position = 50
result = 0

for line in lines:

    direction = line[0]
    number = int(line[1:])

    if direction == "R":
        position += number
    else:
        position -= number

    while position >= 100:
        position -= 100
    while position < 0:
        position += 100

    if position == 0:
        result += 1

print(result)
