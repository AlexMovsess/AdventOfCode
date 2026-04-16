import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay3.txt")) as f:
    content = f.read()
    lines = content.split("\n")

result = 0

for battery in lines:

    first_digit = 0
    second_digit = 0

    for i in range(len(battery) - 1):

        if int(battery[i]) > first_digit:

            first_digit = int(battery[i])
            first_index = i

    for j in range(first_index + 1, len(battery)):

        if int(battery[j]) > second_digit:

            second_digit = int(battery[j])

    result += int(str(first_digit) + str(second_digit))

print(result)
