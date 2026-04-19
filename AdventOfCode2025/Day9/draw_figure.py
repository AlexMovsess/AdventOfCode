import matplotlib.pyplot as plt
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def draw_figure(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    x.append(points[0][0])
    y.append(points[0][1])

    plt.plot(x, y)

    plt.scatter(x[:-1], y[:-1], color="black")

    plt.scatter(points[0][0], points[0][1], color="red", label="Start")
    plt.scatter(points[1][0], points[1][1], color="green", label="Direction")

    plt.legend()
    plt.axis("equal")
    plt.grid(True)
    plt.title("Figure")

    plt.show()


with open(os.path.join(__location__, "AdventOfCodeDay9.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    points = [tuple([int(x) for x in line.split(",")]) for line in lines]

draw_figure(points)
