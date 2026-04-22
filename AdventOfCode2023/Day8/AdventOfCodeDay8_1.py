# --- Day 8: Haunted Wasteland ---

# You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.
# One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.
# It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

# This format defines each node of the network individually. For example:

# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)

# Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

# Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)

# Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?

import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay8.txt"))
tableList = f.read().split("\n\n")
directions = tableList.pop(0)


tableList = [
    (pos, left, right)
    for pos, left, right in re.findall(r"(\w{3}) = \((\w{3}), (\w{3})\)", tableList[0])
]


def findNextPos(string, list):
    for item in list:
        if item[0] == string:
            return item


i = 0
steps = 0
position = findNextPos("AAA", tableList)

while i <= len(directions):
    if directions[i] == "L":
        turn = 1
    else:
        turn = 2
    position = findNextPos(position[turn], tableList)
    if position[0] == "ZZZ":
        steps += 1
        break
    else:
        i += 1
        steps += 1
        if i >= len(directions):
            i -= len(directions)

print("----- Total :", steps, "-----")
