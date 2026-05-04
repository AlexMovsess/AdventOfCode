import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# This is an equation resolution / matrix simplification. number of variables is length of lights. We need to find all solutions and then pick the smallest ?

# (3,4,5,7) (2,4,5,6,7) (1,4,7) (1,3,4,7) (1,2,3,4,5,7) (7) (1,2,3,6) (0,1,3,6,7) {4,59,39,250,242,220,26,250}

total = 0

with open(os.path.join(__location__, "AdventOfCodeDay10.txt")) as f:
    content = f.read()
    lines = content.split("\n")

    for line in lines:

        lights_goal = list(
            map(lambda x: int(x), re.findall(r"\{(.*?)\}", line)[0].split(","))
        )

        buttons = re.findall(r"\((.*?)\)", line)
        buttons = [list(map(int, p.split(","))) for p in buttons]

        finished = False

        lights_goal_copy = lights_goal.copy()

        pushes = 0

        while not finished:
            minimum_light = 10000
            for light in lights_goal_copy:
                if light < minimum_light and light > 0:
                    minimum_light = light
            print(minimum_light)
            min_idx = lights_goal_copy.index(minimum_light)

            for button in buttons:
                if min_idx in button:
                    print(button)

                    wrong_button = False

                    for button_idx in button:
                        if lights_goal_copy[button_idx] - minimum_light < 0:
                            wrong_button = True

                    if not wrong_button:
                        for button_idx in button:
                            lights_goal_copy[button_idx] -= minimum_light
                            pushes += minimum_light
                            print(lights_goal_copy)
                            input()
                        break

# To find minum pushes required you need to start with buttons that are larger and
