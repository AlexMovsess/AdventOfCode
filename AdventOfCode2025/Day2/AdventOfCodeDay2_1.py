import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay2.txt")) as f:
    content = f.read()
    lines = content.split(",")

result = 0


def check_for_invalid_id(id):

    if id[: len(id) // 2] == id[len(id) // 2 :]:
        return True

    else:
        return False


for line in lines:

    id_list = line.split("-")

    id_start = int(id_list[0])
    id_end = int(id_list[1])

    for i in range(id_start, id_end + 1):
        if (
            len(str(i)) % 2 == 0
        ):  # Ignore any id that is composed of an odd number of digits, it cannot be a repetition
            if check_for_invalid_id(str(i)):
                result += i

print(result)
