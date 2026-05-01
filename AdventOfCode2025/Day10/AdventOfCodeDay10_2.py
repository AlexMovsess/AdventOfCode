import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# (3,4,5,7) (2,4,5,6,7) (1,4,7) (1,3,4,7) (1,2,3,4,5,7) (7) (1,2,3,6) (0,1,3,6,7) {4,59,39,250,242,220,26,250}

# This is an equation resolution / matrix simplification. number of variables is length of lights. We need to find all solutions and then pick the smallest ?

total = 0

with open(os.path.join(__location__, "AdventOfCodeDay10.txt")) as f:
    content = f.read()
    lines = content.split("\n")

    for line in lines:

        joltage_goal = list(
            map(lambda x: int(x), re.findall(r"\{(.*?)\}", line)[0].split(","))
        )

        buttons = re.findall(r"\((.*?)\)", line)
        buttons = [list(map(int, p.split(","))) for p in buttons]
        buttons.sort(key=lambda x: len(x), reverse=True)

        finished = False
        pushes = 0

        joltage_goal_copy = joltage_goal.copy()

        while not finished:

            minimum_joltage = 10000000
            if sum(joltage_goal_copy) == 0:
                break

            print(joltage_goal_copy)

            for joltage in joltage_goal_copy:
                print(joltage)
                if joltage < minimum_joltage and joltage > 0:
                    minimum_joltage = joltage

            index_minimum_joltage = joltage_goal_copy.index(minimum_joltage)

            print(buttons)
            print(index_minimum_joltage, minimum_joltage)

            for button in buttons:

                if index_minimum_joltage in button:
                    print(button)
                    print(joltage_goal_copy)
                    right_button = True

                    for index in button:
                        if joltage_goal_copy[index] - minimum_joltage < 0:
                            right_button = False

                    if right_button:
                        for index in button:
                            joltage_goal_copy[index] -= minimum_joltage
                        pushes += minimum_joltage
                    else:
                        continue

                    input()
                    break

        total += pushes
        print(pushes)
print(total)
