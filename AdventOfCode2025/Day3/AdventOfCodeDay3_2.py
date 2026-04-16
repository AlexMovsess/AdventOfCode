import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay3.txt")) as f:
    content = f.read()
    lines = content.split("\n")

result = 0

for battery in lines:

    digit_list = [0] * 12
    index_list = [0] * 12
    index = -1
    remaining_digit = 12

    while remaining_digit > 0:

        for i in range(index + 1, len(battery) - remaining_digit + 1):

            if int(battery[i]) > digit_list[12 - remaining_digit]:

                digit_list[12 - remaining_digit] = int(battery[i])
                index = i

        remaining_digit -= 1

    str_result = ""
    for digit in digit_list:
        str_result += str(digit)
    result += int(str_result)

print(result)
