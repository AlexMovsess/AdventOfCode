import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay2.txt")) as f:
    content = f.read()
    lines = content.split(",")


def multiplicator_decomposition(n):
    """This function returns a list of all possible dividers of a number n, including 1."""
    result_list = []
    for i in range(1, n):
        if not n % i:
            result_list.append(i)
    return result_list


def check_for_invalid_id(id):

    prime_list = multiplicator_decomposition(len(id))

    for (
        divider
    ) in prime_list:  # Check for all possible divisions of the id ex : 1 2 1 2 , 12 12

        for j in range(
            len(id) - 2 * divider + 1
        ):  # Parse the divisions entry by entry. If an entry is different from the precedent, break

            first_pattern = id[j : j + divider]
            second_pattern = id[j + divider : j + 2 * divider]

            if first_pattern != second_pattern:
                break

            if (
                j == len(id) - 2 * divider
            ):  # We have reached the end of the division and all entries are the same. This is an invalid ID.

                return int(id)

    return 0


result_sum = 0

for line in lines:
    id_list = line.split("-")

    id_start = int(id_list[0])
    id_end = int(id_list[1])

    for i in range(id_start, id_end + 1):
        result = check_for_invalid_id(str(i))
        if result:
            result_sum += result

print(result_sum)
