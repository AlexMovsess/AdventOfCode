# --- Part Two ---

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
# Now, a nice string is one with all of the following properties:

#     It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#     It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

# For example:

#     qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
#     xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
#     uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
#     ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

# How many strings are nice under these new rules?

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay5.txt"))
content = f.read()
puzzleList = content.split("\n")[0:-1]

niceStrings = 0

for string in puzzleList:
    doublePair = False
    repetitionAcross = False
    for i in range(2, len(string), 1):
        if string[i - 2 : i] in string[: i - 2] or string[i - 2 : i] in string[i:]:
            doublePair = True
        if string[i] == string[i - 2]:
            repetitionAcross = True
    if doublePair and repetitionAcross:
        niceStrings += 1

print(niceStrings)

# WITH REGEX

print(
    len(
        [
            s
            for s in puzzleList
            if (re.search(r"(..).*\1", s) and re.search(r"(.).\1", s))
        ]
    )
)
