# --- Part Two ---

# As you look out at the field of springs, you feel like there are way more springs than the condition records list. When you examine the records, you discover that they were actually folded up this whole time!
# To unfold the records, on each row, replace the list of spring conditions with five copies of itself (separated by ?) and replace the list of contiguous groups of damaged springs with five copies of itself (separated by ,).

# So, this row:

# .# 1

# Would become:

# .#?.#?.#?.#?.# 1,1,1,1,1

# The first line of the above example would become:
# ???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
# In the above example, after unfolding, the number of possible arrangements for some rows is now much larger:

#     ???.### 1,1,3 - 1 arrangement
#     .??..??...?##. 1,1,3 - 16384 arrangements
#     ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
#     ????.#...#... 4,1,1 - 16 arrangements
#     ????.######..#####. 1,6,5 - 2500 arrangements
#     ?###???????? 3,2,1 - 506250 arrangements

# After unfolding, adding all of the possible arrangement counts together produces 525152.
# Unfold your condition records; what is the new sum of possible arrangement counts?
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay12.txt"))

ways = 0

for line in f:
    record, checksum = line.split()
    checksum = list(map(int, checksum.split(",")))
    record = "?".join([record for i in range(5)])
    checksum *= 5
    positions = {0: 1}
    for i, contiguous in enumerate(checksum):
        print(
            "Going over the conditions :",
            checksum,
            record,
            i,
            contiguous,
        )
        new_positions = {}
        for k, v in positions.items():
            for n in range(
                k, len(record) - sum(checksum[i + 1 :]) + len(checksum[i + 1 :])
            ):
                print("iterations:", k, v, n, "positions:", positions, new_positions)
                input()
                if (
                    n + contiguous - 1 < len(record)
                    and "." not in record[n : n + contiguous]
                ):
                    # If it's possible from this starting char to have the required number of # next including this one and not go over the limit of the record
                    if (
                        i == len(checksum) - 1 and "#" not in record[n + contiguous :]
                    ) or (
                        i < len(checksum) - 1
                        and n + contiguous < len(record)
                        and record[n + contiguous] != "#"
                    ):
                        # If we have reached the end of the checksum and there are no # left OR
                        new_positions[n + contiguous + 1] = (
                            new_positions[n + contiguous + 1] + v
                            if n + contiguous + 1 in new_positions
                            else v
                        )  # Create new value in the dict else add one to the value already here
                if record[n] == "#":
                    break
        positions = new_positions
    ways += sum(positions.values())

print(ways)
