# --- Part Two ---

# The crucibles of lava simply aren't large enough to provide an adequate supply of lava to the machine parts factory. Instead, the Elves are going to upgrade to ultra crucibles.
# Ultra crucibles are even more difficult to steer than normal crucibles. Not only do they have trouble going in a straight line, but they also have trouble turning!
# Once an ultra crucible starts moving in a direction, it needs to move a minimum of four blocks in that direction before it can turn (or even before it can stop at the end). However, it will eventually start to get wobbly: an ultra crucible can move a maximum of ten consecutive blocks without turning.
# In the above example, an ultra crucible could follow this path to minimize heat loss:

# 2>>>>>>>>1323
# 32154535v5623
# 32552456v4254
# 34465858v5452
# 45466578v>>>>
# 143859879845v
# 445787698776v
# 363787797965v
# 465496798688v
# 456467998645v
# 122468686556v
# 254654888773v
# 432267465553v

# In the above example, an ultra crucible would incur the minimum possible heat loss of 94.
# Here's another example:

# 111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991

# Sadly, an ultra crucible would need to take an unfortunate path like this one:

# 1>>>>>>>1111
# 9999999v9991
# 9999999v9991
# 9999999v9991
# 9999999v>>>>

# This route causes the ultra crucible to incur the minimum possible heat loss of 71.
# Directing the ultra crucible from the lava pool to the machine parts factory, what is the least heat loss it can incur?

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from heapq import heappop, heappush as push

G = {
    i + j * 1j: int(c)
    for i, r in enumerate(open(os.path.join(__location__, "AdventOfCodeDay17.txt")))
    for j, c in enumerate(r.strip())
}


def findMinimumPath(min, max, end=[*G][-1], x=0):
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    seen = set()

    while todo:
        val, _, pos, direction = heappop(
            todo
        )  # heapop always takes the smallest. Ensures that we find the fastest route first rather than trying them all.
        if pos == end:
            return val  # if end is reached, return final value of sum

        if (pos, direction) in seen:
            continue  # skip that case if already seen

        seen.add(
            (pos, direction)
        )  # if case not seen, add it to the seen list and treat it
        for d in (
            1j / direction,
            -1j / direction,
        ):  # turn right, turn left from initial position
            for i in range(min, max + 1):
                if (
                    pos + d * i in G
                ):  # for every position between the minimum length and the max
                    v = sum(
                        G[pos + d * j] for j in range(1, i + 1)
                    )  # Add the value of each taken step to the global path value
                    push(
                        todo, (val + v, (x := x + 1), pos + d * i, d)
                    )  # Add all possible starting point to the list to be examninated.


print("----- Total :", findMinimumPath(4, 10), "-----")
