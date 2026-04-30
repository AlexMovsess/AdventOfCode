# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.
# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay5.txt"))
content = f.read()
puzzleList = content.split("\n")[0:-1]

vowelsString = "aeiou"
banList = ["ab", "cd", "pq", "xy"]
niceStrings = 0

for string in puzzleList:
    ban = False
    for bannedStr in banList:
        if bannedStr in string:
            ban = True
    if ban == True:
        continue

    vowels = 0
    previousCharacter = 0
    appearedTwice = False
    for character in string:
        if character in vowelsString:
            vowels += 1
        if character == previousCharacter:
            appearedTwice = True
        else:
            previousCharacter = character
    if vowels >= 3 and appearedTwice:
        niceStrings += 1

print(niceStrings)

# WITH REGEX

print(
    len(
        [
            s
            for s in puzzleList
            if (
                re.search(r"([aeiou].*){3,}", s)
                and re.search(r"(.)\1", s)
                and not re.search(r"ab|cd|pq|xy", s)
            )
        ]
    )
)
