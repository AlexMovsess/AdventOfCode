# --- Day 23: A Long Walk ---

# The Elves resume water filtering operations! Clean water starts flowing over the edge of Island Island.
# They offer to help you go over the edge of Island Island, too! Just hold on tight to one end of this impossibly long rope and they'll lower you down a safe distance from the massive waterfall you just created.
# As you finally reach Snow Island, you see that the water isn't really reaching the ground: it's being absorbed by the air itself. It looks like you'll finally have a little downtime while the moisture builds up to snow-producing levels. Snow Island is pretty scenic, even without any snow; why not take a walk?
# There's a map of nearby hiking trails (your puzzle input) that indicates paths (.), forest (#), and steep slopes (^, >, v, and <).
# For example:

# #.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#

# You're currently on the single path tile in the top row; your goal is to reach the single path tile in the bottom row. Because of all the mist from the waterfall, the slopes are probably quite icy; if you step onto a slope tile, your next step must be downhill (in the direction the arrow is pointing). To make sure you have the most scenic hike possible, never step onto the same tile twice. What is the longest hike you can take?
# In the example above, the longest hike you can take is marked with O, and your starting position is marked S:

# #S#####################
# #OOOOOOO#########...###
# #######O#########.#.###
# ###OOOOO#OOO>.###.#.###
# ###O#####O#O#.###.#.###
# ###OOOOO#O#O#.....#...#
# ###v###O#O#O#########.#
# ###...#O#O#OOOOOOO#...#
# #####.#O#O#######O#.###
# #.....#O#O#OOOOOOO#...#
# #.#####O#O#O#########v#
# #.#...#OOO#OOO###OOOOO#
# #.#.#v#######O###O###O#
# #...#.>.#...>OOO#O###O#
# #####v#.#.###v#O#O###O#
# #.....#...#...#O#O#OOO#
# #.#########.###O#O#O###
# #...###...#...#OOO#O###
# ###.###.#.###v#####O###
# #...#...#.#.>.>.#.>O###
# #.###.###.#.###.#.#O###
# #.....###...###...#OOO#
# #####################O#

# This hike contains 94 steps. (The other possible hikes you could have taken were 90, 86, 82, 82, and 74 steps long.)
# Find the longest hike you can take through the hiking trails listed on your map. How many steps long is the longest hike?


import os
from collections import deque
import copy

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay23.txt"))

G = {i + j * 1j: c for i, r in enumerate(f) for j, c in enumerate(r) if c in ".><^v"}

lastLinePos = int(max([r.real for r in G.keys()]))

queue = deque([(0 + 1j, 0, [])])
allPaths = set()

while queue:
    position, step, donePositions = queue.popleft()
    while position.real != lastLinePos:
        donePositions.append(position)
        step += 1
        nextPositions = [
            position + p
            for p in {1j, -1j, 1, -1}
            if position + p in G.keys() and position + p not in donePositions
        ]
        if len(nextPositions) > 1:
            if position - 1j in nextPositions and G[position - 1j] == ">":
                nextPositions.remove(position - 1j)
            if position + 1j in nextPositions and G[position + 1j] == "<":
                nextPositions.remove(position + 1j)
            if position - 1 in nextPositions and G[position - 1] == "v":
                nextPositions.remove(position - 1)
            if position + 1 in nextPositions and G[position + 1] == "^":
                nextPositions.remove(position + 1)
            if len(nextPositions) > 1:
                position = nextPositions.pop(0)
                for nextPos in nextPositions:
                    queue.append((nextPos, step, copy.deepcopy(donePositions)))
            elif len(nextPositions) == 1:
                position = nextPositions[0]
            else:
                break
        elif len(nextPositions) == 1:
            position = nextPositions[0]
        else:
            break
    if position.real == lastLinePos:
        allPaths.add(step)

print("----- Total :", max(allPaths), "-----")
