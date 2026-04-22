# --- Part Two ---

# The galaxies are much older (and thus much farther apart) than the researcher initially estimated.
# Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.
# (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)
# Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?

import os
import re
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay11.txt"))
tableList = f.read().split("\n")

sum = 0


def mapEmptyLines(array):
    map = []
    for i in range(0, len(array), 1):
        if all(char == "." for char in array[i]):
            print("michel")
            map.append(i)
    return map


for index, line in enumerate(tableList):
    tableList[index] = re.findall(".", tableList[index])

tableList = np.array(tableList)

mapLines = mapEmptyLines(tableList)
tableList = np.transpose(tableList)

mapColumn = mapEmptyLines(tableList)
tableList = np.transpose(tableList)

coordinatesList = []

for i in range(0, len(tableList), 1):
    for j in range(0, len(tableList[i]), 1):
        if tableList[i][j] == "#":
            coordinatesList.append((i, j))

for i in range(0, len(coordinatesList), 1):
    for j in range(i + 1, len(coordinatesList), 1):
        for k in mapLines:
            if coordinatesList[i][0] < k < coordinatesList[j][0]:
                sum += 999999
        for k in mapColumn:
            if (
                coordinatesList[i][1] < k < coordinatesList[j][1]
                or coordinatesList[i][1] > k > coordinatesList[j][1]
            ):
                sum += 999999
        sum += abs((coordinatesList[j][0] - coordinatesList[i][0])) + abs(
            (coordinatesList[j][1] - coordinatesList[i][1])
        )

print("----- Total :", sum, "-----")

# Keep the position of all empty lines. Each times one of these positions is between the first galaxy and the second, add 999999 to the sum.
# Same for columns.
