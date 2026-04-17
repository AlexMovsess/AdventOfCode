import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay7.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    matrix = [line.split() for line in lines]

split_count = 0
rays_set = set()

for line in lines:
    for i in range(len(line)):

        if line[i] == "S":
            rays_set.add(i)
        if line[i] == "^" and rays_set.__contains__(i):
            split_count += 1
            rays_set.remove(i)
            if i != 0:
                rays_set.add(i - 1)
            if i != len(line):
                rays_set.add(i + 1)

print(split_count)
