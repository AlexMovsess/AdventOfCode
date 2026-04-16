import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay4.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    matrix = [list(line) for line in lines]

result = 0

for i in range(len(matrix)):

    for j in range(len(matrix[i])):

        if matrix[i][j] == "@":

            adjacent_box_count = 0

            if i != 0:
                if matrix[i - 1][j] == "@":
                    adjacent_box_count += 1

                if j != 0:
                    if matrix[i - 1][j - 1] == "@":
                        adjacent_box_count += 1

                if j != len(matrix[i]) - 1:
                    if matrix[i - 1][j + 1] == "@":
                        adjacent_box_count += 1

            if i != len(matrix) - 1:
                if matrix[i + 1][j] == "@":
                    adjacent_box_count += 1

                if j != 0:
                    if matrix[i + 1][j - 1] == "@":
                        adjacent_box_count += 1

                if j != len(matrix[i]) - 1:
                    if matrix[i + 1][j + 1] == "@":
                        adjacent_box_count += 1

            if j != 0:
                if matrix[i][j - 1] == "@":
                    adjacent_box_count += 1

            if j != len(matrix[i]) - 1:
                if matrix[i][j + 1] == "@":
                    adjacent_box_count += 1

            if adjacent_box_count < 4:
                result += 1

print(result)
