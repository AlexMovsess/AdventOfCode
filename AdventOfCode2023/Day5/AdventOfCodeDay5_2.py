# --- Part Two ---

# Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.
# The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

# seeds: 79 14 55 13

# This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.
# Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.
# In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.
# Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?

import os
from operator import itemgetter
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay5.txt"))
content = f.read()
segments = content.split("\n\n")
intervals = []

for seed in re.findall(
    r"(\d+) (\d+)", segments[0]
):  # regex, two digits separed by a space. return a list of all seed tuples
    x1, dx = map(int, seed)  # Apply the int function to every item in the seed tuble
    x2 = x1 + dx
    intervals.append((x1, x2, 1))

min_location = float("inf")
while intervals:
    x1, x2, level = intervals.pop()
    if level == 8:
        min_location = min(x1, min_location)
        continue

    for conversion in re.findall(r"(\d+) (\d+) (\d+)", segments[level]):
        z, y1, dy = map(int, conversion)
        y2 = y1 + dy
        diff = z - y1
        if x2 <= y1 or y2 <= x1:  # no overlap
            continue
        if x1 < y1:  # split original interval at y1
            intervals.append((x1, y1, level))
            x1 = y1
        if y2 < x2:  # split original interval at y2
            intervals.append((y2, x2, level))
            x2 = y2
        intervals.append(
            (x1 + diff, x2 + diff, level + 1)
        )  # perfect overlap -> make conversion and let pass to next nevel
        break

    else:
        intervals.append((x1, x2, level + 1))

print("----- Minimum location :", min_location, "-----")
