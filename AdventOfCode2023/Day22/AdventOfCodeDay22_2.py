# --- Part Two ---

# Disintegrating bricks one at a time isn't going to be fast enough. While it might sound dangerous, what you really need is a chain reaction.

# You'll need to figure out the best brick to disintegrate. For each brick, determine how many other bricks would fall if that brick were disintegrated.

# Using the same example as above:

#     Disintegrating brick A would cause all 6 other bricks to fall.
#     Disintegrating brick F would cause only 1 other brick, G, to fall.

# Disintegrating any other brick would cause no other bricks to fall. So, in this example, the sum of the number of other bricks that would fall as a result of disintegrating each brick is 7.

# For each brick, determine how many other bricks would fall if that brick were disintegrated. What is the sum of the number of other bricks that would fall?

from collections import defaultdict
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay22.txt"))
puzzleInput = f.read()

brick = []
for line in puzzleInput.split("\n"):
    a, b = line.split("~")
    a = list(map(int, a.split(",")))
    b = list(map(int, b.split(",")))
    brick.append((a, b))

n = len(brick)

brick.sort(key=lambda x: x[0][2])

highest = defaultdict(lambda: (0, -1))
bad = set()
graph = [[] for i in range(n)]
for idx, b in enumerate(brick):
    mxh = -1
    support_set = set()
    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):
            if highest[x, y][0] + 1 > mxh:
                mxh = highest[x, y][0] + 1
                support_set = {highest[x, y][1]}
            elif highest[x, y][0] + 1 == mxh:
                support_set.add(highest[x, y][1])
    for x in support_set:
        if x != -1:
            graph[x].append(idx)

    if len(support_set) == 1:
        bad.add(support_set.pop())

    fall = b[0][2] - mxh
    if fall > 0:
        b[0][2] -= fall
        b[1][2] -= fall

    for x in range(b[0][0], b[1][0] + 1):
        for y in range(b[0][1], b[1][1] + 1):
            highest[x, y] = (b[1][2], idx)

print(len(brick) - len(bad) + 1)


def count(idx, graph):
    indeg = [0 for __ in range(n)]
    for j in range(n):
        for i in graph[j]:
            indeg[i] += 1
    q = [idx]
    count = -1
    while len(q) > 0:
        count += 1
        x = q.pop()
        for i in graph[x]:
            indeg[i] -= 1
            if indeg[i] == 0:
                q.append(i)

    return count


print(sum(count(x, graph) for x in range(n)))
