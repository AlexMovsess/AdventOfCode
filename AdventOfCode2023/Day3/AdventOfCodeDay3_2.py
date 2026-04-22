# --- Part Two ---

# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.
# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.
# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.
# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.
# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?

import os


def FindNumbers(tableList, i, j):
    int1 = ""
    int1Found = False
    int2 = ""
    for k in range(-1, 2, 1):
        l = -1
        while l < 2:
            try:
                int(tableList[i + k][j + l])
            except:
                l += 1
            else:
                err = True
                while err:
                    try:
                        int(tableList[i + k][j + l])
                    except:
                        err = False
                        l = l + 1
                    else:
                        l -= 1
                err = True
                while err:
                    try:
                        int(tableList[i + k][j + l])
                    except:
                        err = False
                        int1Found = True
                    else:
                        if int1Found == False:
                            int1 += tableList[i + k][j + l]
                        else:
                            int2 += tableList[i + k][j + l]
                        l += 1
    return (int1, int2)


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay3.txt"))
content = f.read()
tableList = content.split("\n")
tableList[0] = list(tableList[0])
result = 0
for i in range(0, len(tableList) - 1, 1):
    tableList[i] = list(tableList[i])
    print("----- Line", i + 1, "-----")
    for j in range(0, len(tableList[i]) - 1, 1):
        if tableList[i][j] == "*":
            int1, int2 = FindNumbers(tableList, i, j)
            print(int1, "*", int2, "-->", result)
            if int2 != "":
                result += int(int1) * int(int2)
print("----- Total :", result, "-----")
