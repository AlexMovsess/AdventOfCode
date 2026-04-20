import os
from sympy import symbols, Eq, solve

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay10.txt")) as f:
    content = f.read()

# This is an equation resolution / matrix simplification. number of variables is length of lights. We need to find all solutions and then pick the smallest ?

# (3,4,5,7) (2,4,5,6,7) (1,4,7) (1,3,4,7) (1,2,3,4,5,7) (7) (1,2,3,6) (0,1,3,6,7) {4,59,39,250,242,220,26,250}

a, b, c, d, e, f, g, h = symbols("a b c d e f g h")

equation_1 = Eq((h), 4)
equation_2 = Eq((c + d + e + g + h), 59)
equation_3 = Eq((b + e + g), 39)
equation_4 = Eq((a + d + e + g + h), 250)
equation_5 = Eq((a + b + c + d + e), 242)
equation_6 = Eq((a + b + e), 220)
equation_7 = Eq((b + g + h), 26)
equation_8 = Eq((a + b + c + d + e + f + h), 250)

solution = solve(
    (
        equation_1,
        equation_2,
        equation_3,
        equation_4,
        equation_5,
        equation_6,
        equation_7,
        equation_8,
    ),
    (a, b, c, d, e, f, g, h),
)
print("Solution:", solution)

print(sum(solution.values()))

# (1,2,3,4,5,6,7,8,9) (1,5) (0,1,3,4,5,6,7,8,9) (4,8,9) (0,6,7,9) (1,6,8) (0,1,2,5,6,7,8) (0,1,2,3,5,7,8,9) (1,2,4,5) {27,79,30,21,45,59,54,36,50,43}

a, b, c, d, e, f, g, h, i, j = symbols("a b c d e f g h i j")

variable_list = [a, b, c, d, e, f, g, h, i]

variable = variable_list[2] + e + g + h
print(variable)
equation_1 = Eq(variable, 27)
equation_2 = Eq((a + b + c + f + g + h + i), 79)
equation_3 = Eq((a + g + h + i), 30)
equation_4 = Eq((a + c + h), 21)
equation_5 = Eq((a + c + d + i), 45)
equation_6 = Eq((a + b + c + g + h + i), 59)
equation_7 = Eq((a + c + e + f + g), 54)
equation_8 = Eq((a + c + e + g + h), 36)
equation_9 = Eq((a + c + d + f + g + h), 50)
equation_10 = Eq((a + c + d + e + h), 43)

solution = solve(
    (
        equation_1,
        equation_2,
        equation_3,
        equation_4,
        equation_5,
        equation_6,
        equation_7,
        equation_8,
        equation_9,
        equation_10,
    ),
    (a, b, c, d, e, f, g, h, i, j),
)
print("Solution:", solution)

print(sum(solution.values()))
