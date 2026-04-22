# --- Part Two ---

# The Elves were right to be concerned; the planned lagoon would be much too small.
# After a few minutes, someone realizes what happened; someone swapped the color and instruction parameters when producing the dig plan. They don't have time to fix the bug; one of them asks if you can extract the correct instructions from the hexadecimal codes.
# Each hexadecimal code is six hexadecimal digits long. The first five hexadecimal digits encode the distance in meters as a five-digit hexadecimal number. The last hexadecimal digit encodes the direction to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
# So, in the above example, the hexadecimal codes can be converted into the true instructions:

#     #70c710 = R 461937
#     #0dc571 = D 56407
#     #5713f0 = R 356671
#     #d2c081 = D 863240
#     #59c680 = R 367720
#     #411b91 = D 266681
#     #8ceee2 = L 577262
#     #caa173 = U 829975
#     #1b58a2 = L 112010
#     #caa171 = D 829975
#     #7807d2 = L 491645
#     #a77fa3 = U 686074
#     #015232 = L 5411
#     #7a21e3 = U 500254

# Digging out this loop and its interior produces a lagoon that can hold an impressive 952408144115 cubic meters of lava.
# Convert the hexadecimal color codes into the correct instructions; if the Elves follow this new dig plan, how many cubic meters of lava could the lagoon hold?

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay18.txt"))

plan = list(map(str.split, f))

directions = {"0": (1, 0), "1": (0, 1), "2": (-1, 0), "3": (0, -1)}
#                   R           D           L               U


def f(steps, pos=0, ans=1):
    for (x, y), n in steps:
        pos += x * n
        ans += y * n * pos + n / 2
        # Green's theorem
        # So starting from the start point and iterating over every step in the loop, every time you step left add the y value of the current position to the integral sum,
        # and every time you step right subtract the y value of the current position from the integral sum.
        # For vertical steps do nothing.
        # It works but I'm not sure why.

    return int(ans)


print(f((directions[c[7]], int(c[2:7], 16)) for _, _, c in plan))
