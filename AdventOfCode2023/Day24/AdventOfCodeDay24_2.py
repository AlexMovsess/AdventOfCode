# --- Part Two ---

# Upon further analysis, it doesn't seem like any hailstones will naturally collide. It's up to you to fix that!
# You find a rock on the ground nearby. While it seems extremely unlikely, if you throw it just right, you should be able to hit every hailstone in a single throw!
# You can use the probably-magical winds to reach any integer position you like and to propel the rock at any integer velocity. Now including the Z axis in your calculations, if you throw the rock at time 0, where do you need to be so that the rock perfectly collides with every hailstone? Due to probably-magical inertia, the rock won't slow down or change direction when it collides with a hailstone.
# In the example above, you can achieve this by moving to position 24, 13, 10 and throwing the rock at velocity -3, 1, 2. If you do this, you will hit every hailstone as follows:

# Hailstone: 19, 13, 30 @ -2, 1, -2
# Collision time: 5
# Collision position: 9, 18, 20

# Hailstone: 18, 19, 22 @ -1, -1, -2
# Collision time: 3
# Collision position: 15, 16, 16

# Hailstone: 20, 25, 34 @ -2, -2, -4
# Collision time: 4
# Collision position: 12, 17, 18

# Hailstone: 12, 31, 28 @ -1, -2, -1
# Collision time: 6
# Collision position: 6, 19, 22

# Hailstone: 20, 19, 15 @ 1, -5, -3
# Collision time: 1
# Collision position: 21, 14, 12

# Above, each hailstone is identified by its initial position and its velocity. Then, the time and position of that hailstone's collision with your rock are given.
# After 1 nanosecond, the rock has exactly the same position as one of the hailstones, obliterating it into ice dust! Another hailstone is smashed to bits two nanoseconds after that. After a total of 6 nanoseconds, all of the hailstones have been destroyed.
# So, at time 0, the rock needs to be at X position 24, Y position 13, and Z position 10. Adding these three coordinates together produces 47. (Don't add any coordinates from the rock's velocity.)
# Determine the exact position and velocity the rock needs to have at time 0 so that it perfectly collides with every hailstone. What do you get if you add up the X, Y, and Z coordinates of that initial position?

import os
import re
import itertools as it

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay24.txt"))

puzzleInput = f.read()
hailList = list(
    map(
        lambda x: (int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])),
        re.findall(r"(\d+), (\d+), (\d+) @ (\-?\d+), (\-?\d+), (\-?\d+)", puzzleInput),
    )
)

PotentialXSet = None
PotentialYSet = None
PotentialZSet = None
for A, B in it.combinations(hailList, 2):
    APX, APY, APZ, AVX, AVY, AVZ = A
    BPX, BPY, BPZ, BVX, BVY, BVZ = B

    if AVX == BVX and abs(AVX) > 100:
        NewXSet = set()
        Difference = BPX - APX
        for v in range(-1000, 1000):
            if v == AVX:
                continue
            if Difference % (v - AVX) == 0:
                NewXSet.add(v)
        if PotentialXSet != None:
            PotentialXSet = PotentialXSet & NewXSet
        else:
            PotentialXSet = NewXSet.copy()
    elif AVY == BVY and abs(AVY) > 100:
        NewYSet = set()
        Difference = BPY - APY
        for v in range(-1000, 1000):
            if v == AVY:
                continue
            if Difference % (v - AVY) == 0:
                NewYSet.add(v)
        if PotentialYSet != None:
            PotentialYSet = PotentialYSet & NewYSet
        else:
            PotentialYSet = NewYSet.copy()
    elif AVZ == BVZ and abs(AVZ) > 100:
        NewZSet = set()
        Difference = BPZ - APZ
        for v in range(-1000, 1000):
            if v == AVZ:
                continue
            if Difference % (v - AVZ) == 0:
                NewZSet.add(v)
        if PotentialZSet != None:
            PotentialZSet = PotentialZSet & NewZSet
        else:
            PotentialZSet = NewZSet.copy()

RVX, RVY, RVZ = PotentialXSet.pop(), PotentialYSet.pop(), PotentialZSet.pop()

APX, APY, APZ, AVX, AVY, AVZ = hailList[0]
BPX, BPY, BPZ, BVX, BVY, BVZ = hailList[1]
MA = (AVY - RVY) / (AVX - RVX)
MB = (BVY - RVY) / (BVX - RVX)
CA = APY - (MA * APX)
CB = BPY - (MB * BPX)
XPos = int((CB - CA) / (MA - MB))
YPos = int(MA * XPos + CA)
Time = (XPos - APX) // (AVX - RVX)
ZPos = APZ + (AVZ - RVZ) * Time

result = XPos + YPos + ZPos

print("----- Total :", result, "-----")

# If standing on a hail we will see the rock travel in a straight line,
# pass through us and two other points on two other pieces of hail that zip by
# there must be two vectors from our hail to the other two collisions (v1 and v2)
# such that v1 = m * v2 where m is some unknown scalar multiplier.
# we can make v1 = v2 by dividing one of the x,y or z components by itself to ensure
# it is equal to 1. Then solve.

# Select three hail so that the relative, x, y or z is all zero
# Hail 0
# 176253337504656, 321166281702430, 134367602892386 @ 190, 8, 338
# Hail 1
# 308344120080284, 193172753823598, 249535698501761 @ 60, 8, 134
# Hail 2
# 307032218923206, 220427490765998, 286976738475573 @ 29, 8, 58

# PX1 + VX1*t = PX2 + VX2*t
# PX1 - PX2 = VX2*t - VX1*t
# (PX1-PX2)/(VX2-VX1) = t

# y = mx + b
# m = avy/avx
# b = apy - m*apx
# m1x + b1 = m2x + b2
# m1x - m2x = b2 - b1
# x = (b2-b1)/(m1-m2)
# 200000000000000
# 400000000000000
