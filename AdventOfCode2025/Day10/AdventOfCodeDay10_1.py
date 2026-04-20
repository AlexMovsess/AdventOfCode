import os
import re
from itertools import combinations

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

total = 0

with open(os.path.join(__location__, "AdventOfCodeDay10.txt")) as f:
    content = f.read()
    lines = content.split("\n")

    for line in lines:

        lights_goal = re.findall(r"\[(.*?)\]", line)[0]
        lights_goal = [i == "#" for i in lights_goal]

        buttons = re.findall(r"\((.*?)\)", line)
        buttons = [list(map(int, p.split(","))) for p in buttons]

        push_count = 1
        found_minimum = False

        while not found_minimum:

            button_combination_list = list(combinations(buttons, push_count))

            for possible_combination in button_combination_list:
                lights = [False] * len(lights_goal)
                for button_pressed in possible_combination:
                    for index in button_pressed:
                        lights[index] = not lights[index]

                if lights == lights_goal:
                    found_minimum = True
                    total += push_count
                    break

            push_count += 1

print(total)

# If you push the same button twice, you get the same input again.
# Do combinations : First combinations of 1 buttons, then combinations of two buttons, then of 3, etc. Order does not matter.
