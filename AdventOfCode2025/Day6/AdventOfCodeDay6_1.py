import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay6.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    matrix = [line.split() for line in lines]

total = 0

for i in range(len(matrix[0])):

    if matrix[4][i] == "+":
        result = (
            int(matrix[0][i])
            + int(matrix[1][i])
            + int(matrix[2][i])
            + int(matrix[3][i])
        )

    else:
        result = (
            int(matrix[0][i])
            * int(matrix[1][i])
            * int(matrix[2][i])
            * int(matrix[3][i])
        )

    total += result

print(total)
