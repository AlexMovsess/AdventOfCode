# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay1.txt"))
DigitList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
content = f.read()
tableList = content.split()
sum = 0
for line in tableList:
    merge = ""
    if any(elem in line for elem in DigitList):
        for i in range(0, len(DigitList)):
            line = line.replace(
                DigitList[i], DigitList[i] + str(i + 1) + DigitList[i]
            )  # numbers maybe fused ex: oneight = 18 or twone = 21. Can't replace a number with its int as it would also replace the second one.
    for i in range(0, len(line)):
        if line[i].isdigit():
            merge += str(line[i])
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            merge += str(line[i])
            break
    sum += int(merge)
print(sum)
