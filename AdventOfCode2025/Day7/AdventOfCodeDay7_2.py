import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay7.txt")) as f:
    content = f.read()
    lines = content.split("\n")

split_count = 0

rays_dict = {}
for k in range(len(lines[0])):
    rays_dict[k] = 0

for line in lines:

    for i in range(len(line)):

        if line[i] == "S":
            rays_dict[i] = 1

        if line[i] == "^" and rays_dict[i] != 0:

            if i != 0:
                rays_dict[i - 1] += rays_dict[i]

            if i != len(line):
                rays_dict[i + 1] += rays_dict[i]

            rays_dict[i] = 0

print(sum(list(rays_dict.values())))

# The idea is that you keep track of precedent timelines in the values of the dict. Each time a split happens, the previous timelines are added to the two new ones.
# It is faster than using a queue and testing all possible timelines.
