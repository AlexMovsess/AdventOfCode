import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay5.txt")) as f:
    content = f.read()
    input_split = content.split("\n\n")
    range_list = input_split[0]

    range_list = range_list.split("\n")
    range_list = [i.split("-") for i in range_list]

range_list.sort(key=lambda x: int(x[0]))
edible_range_list = [range_list.pop(0)]

for start_index_test, end_index_test in range_list:

    for i in range(len(edible_range_list)):

        start_index_true, end_index_true = edible_range_list[i]

        start_index_test = int(start_index_test)
        end_index_test = int(end_index_test)
        start_index_true = int(start_index_true)
        end_index_true = int(end_index_true)

        # The tested range is inside another already accepted range so we discard it
        if end_index_test < end_index_true and start_index_test > start_index_true:
            break

        # The lower bracket of the tested range is inside another already accepted range. We update the upper bracket of the accepted range with the new value
        elif end_index_test >= end_index_true and start_index_test <= end_index_true:
            edible_range_list[i][1] = end_index_test
            break

        # The upper bracket of the tested range is inside another already accepted range. We update the lower bracket of the accepted range with the new value
        elif end_index_test <= end_index_true and start_index_test <= start_index_true:
            edible_range_list[i][0] = start_index_test
            break

        # The tested range is not in any already accepted range so we add it to the list
        else:
            if i == len((edible_range_list)) - 1:
                edible_range_list.append([start_index_test, end_index_test])

result = 0

for start_index_test, end_index_test in edible_range_list:
    result += int(end_index_test) - int(start_index_test)

# We need to add 1 for every range in the list because ranges are inclusive (counts both the right and left bracket) and substractions are not
result += len(edible_range_list)

print(result)
