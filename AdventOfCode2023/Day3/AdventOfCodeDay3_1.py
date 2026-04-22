# --- Day 3: Gear Ratios ---

# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.
# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
# "Aaah!"
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
# Here is an example engine schematic:

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

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay3.txt"))
content = f.read()
tableList = content.split("\n")
tableList[0] = list(tableList[0])
total = 0

for i in range(0, len(tableList) - 1, 1):
    tableList[i] = list(tableList[i])
    print("----- Line", i + 1, "-----")
    j = 0
    while j < len(
        tableList[i]
    ):  # Use a while loop in order to control the incrementation
        try:
            int(tableList[i][j])
        except:  # tableList[i][j] is not an int, next
            j += 1
        else:  # tableList[i][j] is an int
            characterFound = False
            for k in [
                -1,
                0,
                1,
            ]:  # Examine the three items at the left of the int (up-left, middle-left and down-left) for characters
                try:
                    int(tableList[i + k][j - 1])
                except ValueError:
                    if tableList[i + k][j - 1] != ".":
                        characterFound = True
                except IndexError:
                    pass
                else:
                    pass
            err = True
            numberToAdd = ""
            while err:  # Go accross the int until you meet a character again
                try:
                    int(tableList[i][j])
                except ValueError:  # We have reached the end of the int.
                    for k in [
                        -1,
                        0,
                        1,
                    ]:  # Examine the three items at the right of the int (up-right, middle-right and down-right) for characters
                        try:
                            int(tableList[i + k][j])
                        except ValueError:
                            if tableList[i + k][j] != ".":
                                characterFound = True
                        except IndexError:
                            pass
                    if characterFound == True:
                        total += int(numberToAdd)
                        print("Added number:", numberToAdd)
                    err = False
                except IndexError:  # Don't forget ints that end at the end of the line
                    err = False
                    if characterFound:
                        total += int(numberToAdd)
                        print("Added number:", numberToAdd)
                else:  # It is still an int, check above and below for characters
                    for k in [-1, 1]:
                        try:
                            int(tableList[i + k][j])
                        except ValueError:
                            if tableList[i + k][j] != ".":
                                characterFound = True
                        except IndexError:
                            pass
                    numberToAdd += tableList[i][
                        j
                    ]  # Add each digit to the str of the number
                j += 1  # !!! Incrementation of j is done while checking the int in order not to check the same int twice
print("----- Total :", total, "-----")
