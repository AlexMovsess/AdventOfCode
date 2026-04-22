# --- Day 12: Hot Springs ---

# You finally reach the hot springs! You can see steam rising from secluded areas attached to the primary, ornate building.
# As you turn to enter, the researcher stops you. "Wait - I thought you were looking for the hot springs, weren't you?" You indicate that this definitely looks like hot springs to you.
# "Oh, sorry, common mistake! This is actually the onsen! The hot springs are next door."
# You look in the direction the researcher is pointing and suddenly notice the massive metal helixes towering overhead. "This way!"
# It only takes you a few more steps to reach the main gate of the massive fenced-off area containing the springs. You go through the gate and into a small administrative building.
# "Hello! What brings you to the hot springs today? Sorry they're not very hot right now; we're having a lava shortage at the moment." You ask about the missing machine parts for Desert Island.
# "Oh, all of Gear Island is currently offline! Nothing is being manufactured at the moment, not until we get more lava to heat our forges. And our springs. The springs aren't very springy unless they're hot!"
# "Say, could you go up and see why the lava stopped flowing? The springs are too cold for normal operation, but we should be able to find one springy enough to launch you up there!"
# There's just one problem - many of the springs have fallen into disrepair, so they're not actually sure which springs would even be safe to use! Worse yet, their condition records of which springs are damaged (your puzzle input) are also damaged! You'll need to help them repair the damaged records.
# In the giant field just outside, the springs are arranged into rows. For each row, the condition records show every spring and whether it is operational (.) or damaged (#). This is the part of the condition records that is itself damaged; for some springs, it is simply unknown (?) whether the spring is operational or damaged.
# However, the engineer that produced the condition records also duplicated some of this information in a different format! After the list of springs for a given row, the size of each contiguous group of damaged springs is listed in the order those groups appear in the row. This list always accounts for every damaged spring, and each number is the entire size of its contiguous group (that is, groups are always separated by at least one operational spring: #### would always be 4, never 2,2).
# So, condition records with no unknown spring conditions might look like this:

# #.#.### 1,1,3
# .#...#....###. 1,1,3
# .#.###.#.###### 1,3,1,6
# ####.#...#... 4,1,1
# #....######..#####. 1,6,5
# .###.##....# 3,2,1

# However, the condition records are partially damaged; some of the springs' conditions are actually unknown (?). For example:

# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1

# Equipped with this information, it is your job to figure out how many different arrangements of operational and broken springs fit the given criteria in each row.
# In the first line (???.### 1,1,3), there is exactly one way separate groups of one, one, and three broken springs (in that order) can appear in that row: the first three unknown springs must be broken, then operational, then broken (#.#), making the whole row #.#.###.
# The second line is more interesting: .??..??...?##. 1,1,3 could be a total of four different arrangements. The last ? must always be broken (to satisfy the final contiguous group of three broken springs), and each ?? must hide exactly one of the two broken springs. (Neither ?? could be both broken springs or they would form a single contiguous group of two; if that were true, the numbers afterward would have been 2,3 instead.) Since each ?? can either be #. or .#, there are four possible arrangements of springs.
# The last line is actually consistent with ten different arrangements! Because the first number is 3, the first and second ? must both be . (if either were #, the first number would have to be 4 or higher). However, the remaining run of unknown spring conditions have many different ways they could hold groups of two and one broken springs:

# ?###???????? 3,2,1
# .###.##.#...
# .###.##..#..
# .###.##...#.
# .###.##....#
# .###..##.#..
# .###..##..#.
# .###..##...#
# .###...##.#.
# .###...##..#
# .###....##.#

# In this example, the number of possible arrangements for each row is:

#     ???.### 1,1,3 - 1 arrangement
#     .??..??...?##. 1,1,3 - 4 arrangements
#     ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
#     ????.#...#... 4,1,1 - 1 arrangement
#     ????.######..#####. 1,6,5 - 4 arrangements
#     ?###???????? 3,2,1 - 10 arrangements

# Adding all of the possible arrangement counts together produces a total of 21 arrangements.
# For each row, count all of the different arrangements of operational and broken springs that meet the given criteria. What is the sum of those counts?

import os

# import re
# import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay12.txt"))

ways = 0

for line in f:
    record, checksum = line.split()
    checksum = list(map(int, checksum.split(",")))
    positions = {0: 1}
    for i, contiguous in enumerate(checksum):
        print(
            "Going over",
            checksum,
            "with record",
            record,
            "index =",
            i,
            "val = ",
            contiguous,
        )
        new_positions = {}
        for k, v in positions.items():
            print("iterations on items:", k, v, "in", positions)
            for n in range(
                k, len(record) - sum(checksum[i + 1 :]) + len(checksum[i + 1 :])
            ):
                print(
                    "iteration:",
                    n,
                    "over",
                    len(record) - sum(checksum[i + 1 :]) + len(checksum[i + 1 :]),
                    "char =",
                    record[n],
                    "checksum",
                    sum(checksum[i + 1 :]),
                    "len",
                    len(checksum[i + 1 :]),
                )

                if (
                    n + contiguous - 1 < len(record)
                    and "." not in record[n : n + contiguous]
                ):
                    # If it's possible from this starting char to have the required number of # next including this one and not go over the limit of the record
                    print("evaluating over:", record[n : n + contiguous])
                    print(
                        "Condition1:",
                        (i == len(checksum) - 1, "#" not in record[n + contiguous :]),
                    )
                    if n + contiguous < len(record):
                        print(
                            "Condition2:",
                            (
                                i < len(checksum) - 1,
                                n + contiguous,
                                record[n + contiguous] != "#",
                                record[n + contiguous],
                            ),
                        )
                    else:
                        print(
                            "n + contiguous < len(record)", n + contiguous, len(record)
                        )
                    if (
                        i == len(checksum) - 1 and "#" not in record[n + contiguous :]
                    ) or (
                        i < len(checksum) - 1
                        and n + contiguous < len(record)
                        and record[n + contiguous] != "#"
                    ):
                        # If we have reached the end of the checksum and there are no # left OR we have not reached the end and having the desired number of # here will not reach the end and the value after our spot is not an # (meaning our string of # actually stops here)
                        new_positions[n + contiguous + 1] = (
                            new_positions[n + contiguous + 1] + v
                            if n + contiguous + 1 in new_positions
                            else v
                        )
                        # Create new value in the dict else add one to the value already here
                        # The new index to search from is the one after the set of ### and its final point we discovered. ex: ###.?<--
                        print("added a new position :", new_positions)
                input()
                if (
                    record[n] == "#"
                ):  # if we have found a # then the next # string has to start here so we escape the loop.
                    break

        positions = new_positions  # create all possible positions for the next number in records.
    ways += sum(positions.values())
print(ways)
