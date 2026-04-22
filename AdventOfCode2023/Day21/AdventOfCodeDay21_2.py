# --- Part Two ---

# The Elf seems confused by your answer until he realizes his mistake: he was reading from a list of his favorite numbers that are both perfect squares and perfect cubes, not his step counter.
# The actual number of steps he needs to get today is exactly 26501365.
# He also points out that the garden plots and rocks are set up so that the map repeats infinitely in every direction.
# So, if you were to look one additional map-width or map-height out from the edge of the example map above, you would find that it keeps repeating:

# .................................
# .....###.#......###.#......###.#.
# .###.##..#..###.##..#..###.##..#.
# ..#.#...#....#.#...#....#.#...#..
# ....#.#........#.#........#.#....
# .##...####..##...####..##...####.
# .##..#...#..##..#...#..##..#...#.
# .......##.........##.........##..
# .##.#.####..##.#.####..##.#.####.
# .##..##.##..##..##.##..##..##.##.
# .................................
# .................................
# .....###.#......###.#......###.#.
# .###.##..#..###.##..#..###.##..#.
# ..#.#...#....#.#...#....#.#...#..
# ....#.#........#.#........#.#....
# .##...####..##..S####..##...####.
# .##..#...#..##..#...#..##..#...#.
# .......##.........##.........##..
# .##.#.####..##.#.####..##.#.####.
# .##..##.##..##..##.##..##..##.##.
# .................................
# .................................
# .....###.#......###.#......###.#.
# .###.##..#..###.##..#..###.##..#.
# ..#.#...#....#.#...#....#.#...#..
# ....#.#........#.#........#.#....
# .##...####..##...####..##...####.
# .##..#...#..##..#...#..##..#...#.
# .......##.........##.........##..
# .##.#.####..##.#.####..##.#.####.
# .##..##.##..##..##.##..##..##.##.
# .................................

# This is just a tiny three-map-by-three-map slice of the inexplicably-infinite farm layout; garden plots and rocks repeat as far as you can see. The Elf still starts on the one middle tile marked S, though - every other repeated S is replaced with a normal garden plot (.).
# Here are the number of reachable garden plots in this new infinite version of the example map for different numbers of steps:

#     In exactly 6 steps, he can still reach 16 garden plots.
#     In exactly 10 steps, he can reach any of 50 garden plots.
#     In exactly 50 steps, he can reach 1594 garden plots.
#     In exactly 100 steps, he can reach 6536 garden plots.
#     In exactly 500 steps, he can reach 167004 garden plots.
#     In exactly 1000 steps, he can reach 668697 garden plots.
#     In exactly 5000 steps, he can reach 16733044 garden plots.

# However, the step count the Elf needs is much larger! Starting from the garden plot marked S on your infinite map, how many garden plots could the Elf reach in exactly 26501365 steps?

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "AdventOfCodeDay21.txt"))

G = {i + j * 1j: c for i, r in enumerate(f) for j, c in enumerate(r) if c in ".S"}

done = []
todo = {x for x in G if G[x] == "S"}
cmod = lambda x: complex(x.real % 131, x.imag % 131)

for s in range(3 * 131):
    if s % 131 == 65:
        done.append(len(todo))

    todo = {p + d for d in {1, -1, 1j, -1j} for p in todo if cmod(p + d) in G}

print(done)

f = lambda n, a, b, c: a + n * (b - a + (n - 1) * (c - b - b + a) // 2)

print(f(26501365 // 131, *done))
