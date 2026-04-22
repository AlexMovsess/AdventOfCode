# --- Part Two ---

# As you try to work out what might be wrong, the reindeer tugs on your shirt and leads you to a nearby control panel. There, a collection of buttons lets you align the contraption so that the beam enters from any edge tile and heading away from that edge. (You can choose either of two directions for the beam if it starts on a corner; for instance, if the beam starts in the bottom-right corner, it can start heading either left or upward.)
# So, the beam could start on any tile in the top row (heading downward), any tile in the bottom row (heading upward), any tile in the leftmost column (heading right), or any tile in the rightmost column (heading left). To produce lava, you need to find the configuration that energizes as many tiles as possible.
# In the above example, this can be achieved by starting the beam in the fourth tile from the left in the top row:

# .|<2<\....
# |v-v\^....
# .v.v.|->>>
# .v.v.v^.|.
# .v.v.v^...
# .v.v.v^..\
# .v.v/2\\..
# <-2-/vv|..
# .|<<<2-|.\
# .v//.|.v..

# Using this configuration, 51 tiles are energized:

# .#####....
# .#.#.#....
# .#.#.#####
# .#.#.##...
# .#.#.##...
# .#.#.##...
# .#.#####..
# ########..
# .#######..
# .#...#.#..

# Find the initial beam configuration that energizes the largest number of tiles; how many tiles are energized in that configuration?

import os
import re
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay16.txt"))
puzzleList = f.read().split("\n")


def findEnergyFromInput(i, j, direction):
    energizedMap = []
    puzzleMap = []
    for line in puzzleList:
        puzzleMap.append(re.findall(".", line))
        energizedMap.append([0 for k in range(len(line))])

    puzzleMap = np.array(puzzleMap)
    energizedMap = np.array(energizedMap)

    startPosition = [(i, j, direction)]
    usedStartPosition = []

    while len(startPosition) > 0:
        start = startPosition.pop(0)
        if start not in usedStartPosition:
            usedStartPosition.append(start)
            sendBeam(start, energizedMap, puzzleMap, usedStartPosition, startPosition)
    return np.sum(energizedMap)


def sendBeam(
    startPositionTuple, energizedMap, puzzleMap, usedStartPosition, startPosition
):
    i = startPositionTuple[0]
    j = startPositionTuple[1]
    direction = startPositionTuple[2]
    recordedPositions = []
    energizedMap[i][j] = 1
    while (
        (i, j, direction) not in recordedPositions
        and 0 <= j < len(puzzleMap[0])
        and 0 <= i < len(puzzleMap)
    ):
        recordedPositions.append((i, j, direction))
        energizedMap[i][j] = 1
        if direction == "right":
            if puzzleMap[i][j] == "\\":
                if i + 1 < len(puzzleMap):
                    direction = "down"
                    i += 1
                else:
                    break
            elif puzzleMap[i][j] == "/":
                if i - 1 >= 0:
                    direction = "up"
                    i -= 1
                else:
                    break
            elif puzzleMap[i][j] == "|":
                if i - 1 >= 0 and (i, j, "up") not in usedStartPosition + startPosition:
                    startPosition.append((i, j, "up"))
                if (
                    i + 1 < len(puzzleMap)
                    and (i, j, "down") not in usedStartPosition + startPosition
                ):
                    startPosition.append((i, j, "down"))
                break
            else:
                j += 1
        elif direction == "down":
            if puzzleMap[i][j] == "\\":
                if j + 1 < len(puzzleMap[i]):
                    direction = "right"
                    j += 1
                else:
                    break
            elif puzzleMap[i][j] == "/":
                if j - 1 >= 0:
                    direction = "left"
                    j -= 1
                else:
                    break
            elif puzzleMap[i][j] == "-":
                if (
                    j - 1 >= 0
                    and (i, j, "left") not in usedStartPosition + startPosition
                ):
                    startPosition.append((i, j, "left"))
                if (
                    j + 1 < len(puzzleMap[i])
                    and (i, j, "right") not in usedStartPosition + startPosition
                ):
                    startPosition.append((i, j, "right"))
                break
            else:
                i += 1
        elif direction == "left":
            if puzzleMap[i][j] == "\\":
                if i - 1 >= 0:
                    direction = "up"
                    i -= 1
                else:
                    break
            elif puzzleMap[i][j] == "/":
                if i + 1 < len(puzzleMap):
                    direction = "down"
                    i += 1
                else:
                    break
            elif puzzleMap[i][j] == "|":
                if i - 1 >= 0 and (i, j, "up") not in usedStartPosition + startPosition:
                    startPosition.append((i, j, "up"))
                if (
                    i + 1 <= len(puzzleMap)
                    and (i, j, "down") not in usedStartPosition + startPosition
                ):
                    startPosition.append((i, j, "down"))
                break
            else:
                j -= 1
        elif direction == "up":
            if puzzleMap[i][j] == "\\":
                if j - 1 >= 0:
                    direction = "left"
                    j -= 1
                else:
                    break
            elif puzzleMap[i][j] == "/":
                if j + 1 < len(puzzleMap[i]):
                    direction = "right"
                    j += 1
                else:
                    break
            elif puzzleMap[i][j] == "-":
                if (
                    j - 1 >= 0
                    and (i, j, "left") not in usedStartPosition + startPosition
                ):
                    startPosition.append((i, j, "left"))
                if (
                    j + 1 < len(puzzleMap[i])
                    and (i, j, "right") not in usedStartPosition + startPosition
                ):
                    startPosition.append((i, j, "right"))
                break
            else:
                i -= 1


maxEnergy = 0

for k in range(0, len(puzzleList)):
    rightK = findEnergyFromInput(k, 0, "right")
    downK = findEnergyFromInput(0, k, "down")
    leftK = findEnergyFromInput(k, len(puzzleList) - 1, "left")
    upK = findEnergyFromInput(len(puzzleList) - 1, k, "up")
    if downK > maxEnergy:
        maxEnergy = downK
    elif rightK > maxEnergy:
        maxEnergy = rightK
    elif leftK > maxEnergy:
        maxEnergy = leftK
    elif upK > maxEnergy:
        maxEnergy = upK

print("----- Total :", maxEnergy, "-----")
