# --- Part Two ---

# You quickly reach the farthest point of the loop, but the animal never emerges. Maybe its nest is within the area enclosed by the loop?
# To determine whether it's even worth taking the time to search for such a nest, you should calculate how many tiles are contained within the loop. For example:

# ...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ...........

# The above loop encloses merely four tiles - the two pairs of . in the southwest and southeast (marked I below). The middle . tiles (marked O below) are not in the loop. Here is the same loop again with those regions marked:

# ...........
# .S-------7.
# .|F-----7|.
# .||OOOOO||.
# .||OOOOO||.
# .|L-7OF-J|.
# .|II|O|II|.
# .L--JOL--J.
# .....O.....

# In fact, there doesn't even need to be a full tile path to the outside for tiles to count as outside the loop - squeezing between pipes is also allowed! Here, I is still within the loop and O is still outside the loop:

# ..........
# .S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........

# In both of the above examples, 4 tiles are enclosed by the loop.

# Here's a larger example:

# .F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...

# The above sketch has many random bits of ground, some of which are in the loop (I) and some of which are outside it (O):

# OF----7F7F7F7F-7OOOO
# O|F--7||||||||FJOOOO
# O||OFJ||||||||L7OOOO
# FJL7L7LJLJ||LJIL-7OO
# L--JOL7IIILJS7F-7L7O
# OOOOF-JIIF7FJ|L7L7L7
# OOOOL7IF7||L7|IL7L7|
# OOOOO|FJLJ|FJ|F7|OLJ
# OOOOFJL-7O||O||||OOO
# OOOOL---JOLJOLJLJOOO

# In this larger example, 8 tiles are enclosed by the loop.

# Any tile that isn't part of the main loop can count as being enclosed by the loop. Here's another example with many bits of junk pipe lying around that aren't connected to the main loop at all:

# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L

# Here are just the tiles that are enclosed by the loop marked with I:

# FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJIF7FJ-
# L---JF-JLJIIIIFJLJJ7
# |F|F-JF---7IIIL7L|7|
# |FFJF7L7F-JF7IIL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L

# In this last example, 10 tiles are enclosed by the loop.

# Figure out whether you have time to search for the nest by calculating the area within the loop. How many tiles are enclosed by the loop?

import os
import sys
from operator import itemgetter

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay10.txt"))
tableList = f.read().split("\n")
lineMarker = [[] for k in range(0, len(tableList), 1)]


def findStartPosition(table):
    for i in range(0, len(table), 1):
        for j in range(0, len(table[i]), 1):
            if table[i][j] == "S":
                return (i, j)


def findNextPosition(
    position, previousPosition, steps
):  # Very brute force, go across the whole loop and divide number of steps by 2.
    char = tableList[position[0]][position[1]]
    lineMarker[position[0]].append((position[1], char))
    if char == "J":
        if previousPosition[0] < position[0]:  # from up
            return findNextPosition(
                (position[0], position[1] - 1), position, steps + 1
            )  # go left
        else:  # from left
            return findNextPosition(
                (position[0] - 1, position[1]), position, steps + 1
            )  # go up
    elif char == "7":
        if previousPosition[0] > position[0]:  # from down
            return findNextPosition(
                (position[0], position[1] - 1), position, steps + 1
            )  # go left
        else:  # from left
            return findNextPosition(
                (position[0] + 1, position[1]), position, steps + 1
            )  # go down
    elif char == "-":
        if previousPosition[1] > position[1]:  # from right
            return findNextPosition(
                (position[0], position[1] - 1), position, steps + 1
            )  # go left
        else:  # from left
            return findNextPosition(
                (position[0], position[1] + 1), position, steps + 1
            )  # go right
    elif char == "|":
        if previousPosition[0] < position[0]:  # from up
            return findNextPosition(
                (position[0] + 1, position[1]), position, steps + 1
            )  # go down
        else:  # from down
            return findNextPosition(
                (position[0] - 1, position[1]), position, steps + 1
            )  # go up
    elif char == "L":
        if previousPosition[0] < position[0]:  # from up
            return findNextPosition(
                (position[0], position[1] + 1), position, steps + 1
            )  # go right
        else:  # from right
            return findNextPosition(
                (position[0] - 1, position[1]), position, steps + 1
            )  # go up
    elif char == "F":
        if previousPosition[0] > position[0]:  # from down
            return findNextPosition(
                (position[0], position[1] + 1), position, steps + 1
            )  # go right
        else:  # from right
            return findNextPosition(
                (position[0] + 1, position[1]), position, steps + 1
            )  # go down
    elif char == "S":
        return steps // 2


sys.setrecursionlimit(20000)  # Default recursion limit for python is a 1000.

x, y = findStartPosition(tableList)
position = (x, y + 1)
previousPosition = (x, y)
findNextPosition(position, previousPosition, 1)

sum = 0

for (
    line
) in (
    lineMarker
):  # We have a matrix with the column number and the corresponding character of every character in the loop on each line. Iterate through every line while counting the inside squares.
    i = 0
    inside = False
    startedInside = False
    startPoint = 0
    while i < len(line):
        column, char = sorted(line, key=itemgetter(0))[i]
        if char == "S":
            char = "F"  # Disgusting yet effective
        if char in ["F", "L"]:  # We are now on the perimeter of the loop.
            startedInside = inside
            startChar = char
            if inside:
                inside = False
                sum += column - startPoint - 1
            while char not in [
                "J",
                "7",
            ]:  # Find the next relevant char. '-' changes nothing, still on perimeter. Only 'J' and '7' will either get us back inside the loop or outside of it.
                i += 1
                column, char = sorted(line, key=itemgetter(0))[i]
            if char == "J":
                if (startChar == "L" and startedInside) or (
                    startChar == "F" and not startedInside
                ):  # Ex: (outside)F - - - J(inside)
                    inside = True
                    startPoint = column
            elif char == "7":  # Ex: (outside)F - - - 7(outside)
                if (startChar == "L" and not startedInside) or (
                    startChar == "F" and startedInside
                ):
                    inside = True
                    startPoint = column
        elif char == "|":
            if inside:
                inside = False
                sum += column - startPoint - 1
            else:
                inside = True
                startPoint = column
        i += 1
print(sum)
