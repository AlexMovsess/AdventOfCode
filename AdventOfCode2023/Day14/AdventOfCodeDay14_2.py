# --- Part Two ---

# The parabolic reflector dish deforms, but not in a way that focuses the beam. To do that, you'll need to move the rocks to the edges of the platform. Fortunately, a button on the side of the control panel labeled "spin cycle" attempts to do just that!
# Each cycle tilts the platform four times so that the rounded rocks roll north, then west, then south, then east. After each tilt, the rounded rocks roll as far as they can before the platform tilts in the next direction. After one cycle, the platform will have finished rolling the rounded rocks in those four directions in that order.
# Here's what happens in the example above after each of the first few cycles:

# After 1 cycle:
# .....#....
# ....#...O#
# ...OO##...
# .OO#......
# .....OOO#.
# .O#...O#.#
# ....O#....
# ......OOOO
# #...O###..
# #..OO#....

# After 2 cycles:
# .....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #..OO###..
# #.OOO#...O

# After 3 cycles:
# .....#....
# ....#...O#
# .....##...
# ..O#......
# .....OOO#.
# .O#...O#.#
# ....O#...O
# .......OOO
# #...O###.O
# #.OOO#...O

# This process should work if you leave it running long enough, but you're still worried about the north support beams. To make sure they'll survive for a while, you need to calculate the total load on the north support beams after 1000000000 cycles.
# In the above example, after 1000000000 cycles, the total load on the north support beams is 64.
# Run the spin cycle for 1000000000 cycles. Afterward, what is the total load on the north support beams?

import numpy as np
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay14.txt"))
m = np.genfromtxt(f, dtype=bytes, comments=None, delimiter=1).astype(str)


def show(m):
    print(
        "----- Total :",
        np.sum(m == "O", axis=1) @ np.arange(m.shape[0], 0, -1),
        "-----",
    )
    # Compte de tous les char 'O' sur une colonne multiplié par le numéro de ladite colonne en commençant par la fin.
    # @ est un opérateur de multiplication matricielle.


def tilt(m):
    for offset in range(1, m.shape[0]):  # De la deuxième ligne à la dernière
        for row in range(
            m.shape[0] - offset
        ):  # De la première ligne à la dernière encore modifiable.
            selection = (m[row, :] == ".") & (m[row + 1, :] == "O")
            # Creates an array of bool that is true where there is an empty space and there is an 'O' on the next line
            # Comma is used as a postion in numpy arrays. m[a,b] == m[a][b]. You can input arrays as a and b and get all values of said array modified.
            m[row, selection] = (
                "O"  # Ex: all values in the row, but only those that are true in selection get transformed into 'O' in row.
            )
            m[row + 1, selection] = (
                "."  # All values in the row, but only those that are also true in selection, get transformed into '.' in row+1
            )
            # At every row loop, we take a line and move all 'O' that can be moved from the next line to it.
        # At the end of this loop, every 'O' has been moved up by one line if possible, wich is why we have an offset.
        # We do not need to move 'O' from last line since they either can't be moved or already have been.


cycles, lookup, found, i = 1000000000 * 4, {}, False, 0
while i < cycles:  # Go faire 1 million de cycles
    tilt(np.rot90(m, -i % 4))
    if i == 0:  # Solution to the first part
        show(m)
    if (
        found == False
    ):  # Keep going as long as you haven't found a repetitive cycle in the million tilt
        check = hash(m.data.tobytes())  # Store as bytes for speed
        if check in lookup:  # If a previous occurence of the cycle has been found
            found = True
            i = cycles - (cycles - i) % (i - lookup[check])
            # 4000000 - (4000000 - 37)%(37 - 9)
            # nbCycle - (nbCycle - iterationNb)%(iterationNb - repetitionStart)
            # nbCycle - totalIterationRestantes%iterationDanscycle
            # nbCyle - ResteIterationsHorsCycle
            # i = Position après que toutes les itérations cycliques aient été faites
            # Just keep tilting to 1 million
        else:
            lookup[check] = (
                i  # We store that particular format of the matrix in a dict if it hasn't been found yet.
            )
    i += 1
show(m)
