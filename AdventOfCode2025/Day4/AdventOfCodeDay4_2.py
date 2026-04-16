import os
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay4.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    matrix = [list(line) for line in lines]


def parse_matrix(matrix):

    result = 0
    new_matrix = copy.deepcopy(matrix)

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
                    new_matrix[i][j] = "."
                    result += 1

    return new_matrix, result


new_matrix, result = parse_matrix(matrix)
total = result

while result != 0:
    new_matrix, result = parse_matrix(new_matrix)
    total += result

print(total)
