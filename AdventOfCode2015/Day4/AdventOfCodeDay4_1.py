import os
import hashlib

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay4.txt"))
content = f.read()[0:-1]

k = 1
while True:
    secretKey = content + str(k)
    if hashlib.md5(secretKey.encode()).hexdigest()[0:5] == "00000":
        print(k)
        break
    else:
        k += 1
