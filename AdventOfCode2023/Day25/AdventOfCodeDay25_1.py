# --- Day 25: Snowverload ---

# Still somehow without snow, you go to the last place you haven't checked: the center of Snow Island, directly below the waterfall.

# Here, someone has clearly been trying to fix the problem. Scattered everywhere are hundreds of weather machines, almanacs, communication modules, hoof prints, machine parts, mirrors, lenses, and so on.

# Somehow, everything has been wired together into a massive snow-producing apparatus, but nothing seems to be running. You check a tiny screen on one of the communication modules: Error 2023. It doesn't say what Error 2023 means, but it does have the phone number for a support line printed on it.

# "Hi, you've reached Weather Machines And So On, Inc. How can I help you?" You explain the situation.

# "Error 2023, you say? Why, that's a power overload error, of course! It means you have too many components plugged in. Try unplugging some components and--" You explain that there are hundreds of components here and you're in a bit of a hurry.

# "Well, let's see how bad it is; do you see a big red reset button somewhere? It should be on its own module. If you push it, it probably won't fix anything, but it'll report how overloaded things are." After a minute or two, you find the reset button; it's so big that it takes two hands just to get enough leverage to push it. Its screen then displays:

# SYSTEM OVERLOAD!

# Connected components would require
# power equal to at least 100 stars!

# "Wait, how many components did you say are plugged in? With that much equipment, you could produce snow for an entire--" You disconnect the call.

# You have nowhere near that many stars - you need to find a way to disconnect at least half of the equipment here, but it's already Christmas! You only have time to disconnect three wires.

# Fortunately, someone left a wiring diagram (your puzzle input) that shows how the components are connected. For example:

# jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr

# Each line shows the name of a component, a colon, and then a list of other components to which that component is connected. Connections aren't directional; abc: xyz and xyz: abc both represent the same configuration. Each connection between two components is represented only once, so some components might only ever appear on the left or right side of a colon.

# In this example, if you disconnect the wire between hfx/pzl, the wire between bvb/cmg, and the wire between nvd/jqt, you will divide the components into two separate, disconnected groups:

#     9 components: cmg, frs, lhk, lsr, nvd, pzl, qnr, rsh, and rzs.
#     6 components: bvb, hfx, jqt, ntq, rhn, and xhk.

# Multiplying the sizes of these groups together produces 54.

# Find the three wires you need to disconnect in order to divide the components into two separate groups. What do you get if you multiply the sizes of these two groups together?
import os
import re
import networkx as nx
from matplotlib import pyplot as plt
from collections import Counter
from operator import itemgetter
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay25.txt"))
puzzleInput = f.read()

mapDict = {x[0]: x[1].split(" ") for x in re.findall(r"(\w+): (.+)\n?", puzzleInput)}

edgesList = []
fullMapDict = {}

# Create a full map of the liaisons, fullMapDict contains all the possible nodes (even the ones that are only outputs) and all the node they are attached to (even in reverse)

for index, items in mapDict.items():
    for item in items:
        edgesList.append((index, item))
        try:
            fullMapDict[item].append(index)
        except KeyError:
            fullMapDict[item] = [index]
        try:
            fullMapDict[index].append(item)
        except KeyError:
            fullMapDict[index] = [item]

# This idea is weird but works : since there are 3 liaisons that can be cut in the graph to separate it in two, it means if you find the shortest path between any two points, it is more likely to go through said liaisons.
# Then you just need to do it enough times to get a great difference of counting passages in liaisons bewteen the ones that are on the same part and the "joining" liaisons.
# Weirdly enough, since it needs a great number of passage, it does not work on the example, only on the real input.

graph = nx.Graph()
graph.add_edges_from(edgesList)

paths = []
nodeList = list(fullMapDict.keys())
for i in range(0, len(nodeList) - 1, 1):
    paths += nx.shortest_path(graph, nodeList[i], nodeList[i + 1])

cutNodeList = list(
    map(
        lambda x: x[0],
        sorted(Counter(paths).items(), key=itemgetter(1), reverse=True)[:6],
    )
)

# We count occurence of nodes in the shortest path between a reduced number of points (for speed).
# The nodes that occurs the most are the ones that are each end of the "joining liaisons".
# Better, nodes that are at the end of the same liaison have roughly the same number of travels.

nodeList1 = []
nodeList2 = []
cutNodeDict = {}

for item in cutNodeList:
    for node in mapDict[item]:
        if node in cutNodeList:
            cutNodeDict[item] = node


def fillSameGroupNodeDict(myList, node):
    if node not in myList:
        myList.append(node)
    try:
        outputList = fullMapDict[node]
    except KeyError:
        pass
    else:
        for output in outputList:
            if output not in myList and not (
                output in cutNodeList and node in cutNodeList
            ):
                fillSameGroupNodeDict(myList, output)


# Take a node at one end and another at the other. Find every related node for each by recurrence.

for node1, node2 in cutNodeDict.items():
    fillSameGroupNodeDict(nodeList1, node1)
    fillSameGroupNodeDict(nodeList2, node2)

try:
    assert len(nodeList1) + len(nodeList2) == len(fullMapDict)
except AssertionError:
    print("ERROR : Number of nodes is not right.")
    print("There are", len(fullMapDict), "nodes total.")
    print(
        "However we have found",
        len(nodeList1),
        "nodes on one side and",
        len(nodeList2),
        "nodes on the other side for a total of",
        len(nodeList1) + len(nodeList2),
        "nodes",
    )
    raise SystemExit

print("----- Total :", len(nodeList2) * len(nodeList1), "-----")

# For more efficiency see : https://en.wikipedia.org/wiki/Karger%27s_algorithm

# Solution fully using networkx :
# G = nx.Graph()
# G.add_edges_from((k,i) for r in f for k,v in [r.split(':')] for i in v.split())
# G.remove_edges_from(nx.minimum_edge_cut(G))
# print(prod(map(len, nx.connected_components(G))))
