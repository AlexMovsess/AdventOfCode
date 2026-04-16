import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay5.txt")) as f:
    content = f.read()
    input_split = content.split("\n\n")
    range_list, ingredient_id_list = input_split[0], input_split[1]

    ingredient_id_list = ingredient_id_list.split("\n")

    range_list = range_list.split("\n")
    range_list = [i.split("-") for i in range_list]

result = 0

for ingredient_id in ingredient_id_list:
    for start_index, end_index in range_list:
        if int(start_index) < int(ingredient_id) < int(end_index):
            result += 1
            break

print(result)
