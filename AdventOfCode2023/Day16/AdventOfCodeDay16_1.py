# --- Day 16: The Floor Will Be Lava ---

# With the beam of light completely focused somewhere, the reindeer leads you deeper still into the Lava Production Facility. At some point, you realize that the steel facility walls have been replaced with cave, and the doorways are just cave, and the floor is cave, and you're pretty sure this is actually just a giant cave.
# Finally, as you approach what must be the heart of the mountain, you see a bright light in a cavern up ahead. There, you discover that the beam of light you so carefully focused is emerging from the cavern wall closest to the facility and pouring all of its energy into a contraption on the opposite side.
# Upon closer inspection, the contraption appears to be a flat, two-dimensional square grid containing empty space (.), mirrors (/ and \), and splitters (| and -).
# The contraption is aligned so that most of the beam bounces around the grid, but each tile on the grid converts some of the beam's light into heat to melt the rock in the cavern.
# You note the layout of the contraption (your puzzle input). For example:

# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....

# The beam enters in the top-left corner from the left and heading to the right. Then, its behavior depends on what it encounters as it moves:

#     If the beam encounters empty space (.), it continues in the same direction.
#     If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror. For instance, a rightward-moving beam that encounters a / mirror would continue upward in the mirror's column, while a rightward-moving beam that encounters a \ mirror would continue downward from the mirror's column.
#     If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
#     If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.

# Beams do not interact with other beams; a tile can have many beams passing through it at the same time. A tile is energized if that tile has at least one beam pass through it, reflect in it, or split in it.
# In the above example, here is how the beam of light bounces around the contraption:

# >|<<<\....
# |v-.\^....
# .v...|->>>
# .v...v^.|.
# .v...v^...
# .v...v^..\
# .v../2\\..
# <->-/vv|..
# .|<<<2-|.\
# .v//.|.v..

# Beams are only shown on empty tiles; arrows indicate the direction of the beams. If a tile contains beams moving in multiple directions, the number of distinct directions is shown instead. Here is the same diagram but instead only showing whether a tile is energized (#) or not (.):

# ######....
# .#...#....
# .#...#####
# .#...##...
# .#...##...
# .#...##...
# .#..####..
# ########..
# .#######..
# .#...#.#..

# Ultimately, in this example, 46 tiles become energized.
# The light isn't energizing enough tiles to produce lava; to debug the contraption, you need to start by analyzing the current situation. With the beam starting in the top-left heading right, how many tiles end up being energized?

import os
import re
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay16.txt"))
puzzleList = f.read().split("\n")

energizedMap = []
puzzleMap = []
for line in puzzleList:
    puzzleMap.append(re.findall(".", line))
    energizedMap.append([0 for k in range(len(line))])

puzzleMap = np.array(puzzleMap)
energizedMap = np.array(energizedMap)

startPosition = [(0, 0, "right")]
usedStartPosition = []


def sendBeam(startPositionTuple):
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


while len(startPosition) > 0:
    start = startPosition.pop(0)
    if start not in usedStartPosition:
        usedStartPosition.append(start)
        sendBeam(start)

print("----- Total :", np.sum(energizedMap), "-----")
