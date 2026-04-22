# --- Day 17: Clumsy Crucible ---

# The lava starts flowing rapidly once the Lava Production Facility is operational. As you leave, the reindeer offers you a parachute, allowing you to quickly reach Gear Island.
# As you descend, your bird's-eye view of Gear Island reveals why you had trouble finding anyone on your way up: half of Gear Island is empty, but the half below you is a giant factory city!
# You land near the gradually-filling pool of lava at the base of your new lavafall. Lavaducts will eventually carry the lava throughout the city, but to make use of it immediately, Elves are loading it into large crucibles on wheels.
# The crucibles are top-heavy and pushed by hand. Unfortunately, the crucibles become very difficult to steer at high speeds, and so it can be hard to go in a straight line for very long.
# To get Desert Island the machine parts it needs as soon as possible, you'll need to find the best way to get the crucible from the lava pool to the machine parts factory. To do this, you need to minimize heat loss while choosing a route that doesn't require the crucible to go in a straight line for too long.
# Fortunately, the Elves here have a map (your puzzle input) that uses traffic patterns, ambient temperature, and hundreds of other parameters to calculate exactly how much heat loss can be expected for a crucible entering any particular city block.
# For example:

# 2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533

# Each city block is marked by a single digit that represents the amount of heat loss if the crucible enters that block. The starting point, the lava pool, is the top-left city block; the destination, the machine parts factory, is the bottom-right city block. (Because you already start in the top-left block, you don't incur that block's heat loss unless you leave that block and then return to it.)
# Because it is difficult to keep the top-heavy crucible going in a straight line for very long, it can move at most three blocks in a single direction before it must turn 90 degrees left or right. The crucible also can't reverse direction; after entering each city block, it may only turn left, continue straight, or turn right.
# One way to minimize heat loss is this path:

# 2>>34^>>>1323
# 32v>>>35v5623
# 32552456v>>54
# 3446585845v52
# 4546657867v>6
# 14385987984v4
# 44578769877v6
# 36378779796v>
# 465496798688v
# 456467998645v
# 12246868655<v
# 25465488877v5
# 43226746555v>

# This path never moves more than three consecutive blocks in the same direction and incurs a heat loss of only 102.
# Directing the crucible from the lava pool to the machine parts factory, but not moving more than three consecutive blocks in the same direction, what is the least heat loss it can incur?


import os
import numpy as np

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


print("----- Total :", findMinimumPath(1, 3), "-----")
