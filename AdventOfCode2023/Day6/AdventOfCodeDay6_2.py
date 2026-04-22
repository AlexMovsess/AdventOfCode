# --- Part Two ---

# As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

# So, the example from before:

# Time:      7  15   30
# Distance:  9  40  200

# ...now instead means this:

# Time:      71530
# Distance:  940200

# Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

# How many ways can you beat the record in this one much longer race?

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay6.txt"))
content = f.read()
tableList = content.split("\n")

time = ""
for k in re.findall(r"(\d+)", tableList[0]):
    time += k
distance = ""
for k in re.findall(r"(\d+)", tableList[1]):
    distance += k

result = 0

for j in range(1, int(time), 1):
    if (int(time) - j) * j >= int(distance):
        result += 1

print("----- Total :", result, "-----")

# Very Brute-force
# There is probably a way to optimize it by searching the first number that satisfies if condition from both ends and returning the difference
