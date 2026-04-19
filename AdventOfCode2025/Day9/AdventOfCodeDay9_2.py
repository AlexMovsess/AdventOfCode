import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay9.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    coordinates = [[tuple([int(x) for x in line.split(",")])] for line in lines]


def calculateArea(coordinates1, coordinates2):
    area = (abs(coordinates1[0] - coordinates2[0]) + 1) * (
        abs(coordinates1[1] - coordinates2[1]) + 1
    )
    return area


def calculateDirection(p0, p1, p2):
    v1x = float(p1[0]) - float(p0[0])
    v1y = float(p1[1]) - float(p0[1])
    v2x = float(p2[0]) - float(p1[0])
    v2y = float(p2[1]) - float(p1[1])

    if v1x * v2y - v1y * v2x > 0.0:
        return -1  # Left turn
    else:
        return 1  # Right turn


# function to check if point q lies on line segment 'pr'
def onSegment(p, q, r):
    return (
        q[0] <= max(p[0], r[0])
        and q[0] >= min(p[0], r[0])
        and q[1] <= max(p[1], r[1])
        and q[1] >= min(p[1], r[1])
    )


# function to find orientation of ordered triplet (p, q, r)
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    # collinear
    if val == 0:
        return 0

    # clock or counterclock wise
    # 1 for clockwise, 2 for counterclockwise
    return 1 if val > 0 else 2


# function to check if two line segments intersect
def doIntersect(segment1, segment2):
    # find the four orientations needed
    # for general and special cases
    o1 = orientation(segment1[0], segment1[1], segment2[0])
    o2 = orientation(segment1[0], segment1[1], segment2[1])
    o3 = orientation(segment2[0], segment2[1], segment1[0])
    o4 = orientation(segment2[0], segment2[1], segment1[1])

    # general case
    if o1 != o2 and o3 != o4:
        return True

    # special cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and onSegment(segment1[0], segment2[0], segment1[1]):
        return True

    # p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and onSegment(segment1[0], segment2[1], segment1[1]):
        return True

    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and onSegment(segment2[0], segment1[0], segment2[1]):
        return True

    # p2, q2 and q1 are collinear and q1 lies on segment p2q2
    if o4 == 0 and onSegment(segment2[0], segment1[1], segment2[1]):
        return True

    return False


side_count = 0

for i in range(-1, len(coordinates) - 1):

    direction = calculateDirection(
        coordinates[i - 1][0], coordinates[i][0], coordinates[i + 1][0]
    )
    side_count += direction

    if coordinates[i][0][0] - coordinates[i - 1][0][0] > 0:
        # right
        if direction == 1:
            list_direction = [4, 1, 2]
        else:
            list_direction = [4]

    elif coordinates[i][0][0] - coordinates[i - 1][0][0] < 0:
        # left
        if direction == 1:
            list_direction = [2, 3, 4]
        else:
            list_direction = [2]

    elif coordinates[i][0][1] - coordinates[i - 1][0][1] > 0:
        # up
        if direction == 1:
            list_direction = [3, 4, 1]
        else:
            list_direction = [3]

    elif coordinates[i][0][1] - coordinates[i - 1][0][1] < 0:
        # down
        if direction == 1:
            list_direction = [1, 2, 3]
        else:
            list_direction = [1]

    coordinates[i].append(list_direction)

# Directions :
# 4 | 1
# -----
# 3 | 2

# If side_count is 4, it is a right rotation (4 right turns total), otherwise its a left rotation. The figure is a square (4 angles) with more alternating turns in between.
# Mine is a left rotation, I will not do both cases, you will need to adapt the algorithm to your use case.

maximum_area = 0


for i in range(0, len(coordinates) - 1):
    for j in range(i + 1, len(coordinates)):

        if (
            1 not in coordinates[i][1]
            and coordinates[j][0][0] > coordinates[i][0][0]
            and coordinates[j][0][1] > coordinates[i][0][1]
        ):
            continue
        if (
            2 not in coordinates[i][1]
            and coordinates[j][0][0] > coordinates[i][0][0]
            and coordinates[j][0][1] < coordinates[i][0][1]
        ):
            continue
        if (
            3 not in coordinates[i][1]
            and coordinates[j][0][0] < coordinates[i][0][0]
            and coordinates[j][0][1] < coordinates[i][0][1]
        ):
            continue
        if (
            4 not in coordinates[i][1]
            and coordinates[j][0][0] < coordinates[i][0][0]
            and coordinates[j][0][1] > coordinates[i][0][1]
        ):
            continue

        if (
            1 not in coordinates[j][1]
            and coordinates[i][0][0] > coordinates[j][0][0]
            and coordinates[i][0][1] > coordinates[j][0][1]
        ):
            continue
        if (
            2 not in coordinates[j][1]
            and coordinates[i][0][0] > coordinates[j][0][0]
            and coordinates[i][0][1] < coordinates[j][0][1]
        ):
            continue
        if (
            3 not in coordinates[j][1]
            and coordinates[i][0][0] < coordinates[j][0][0]
            and coordinates[i][0][1] < coordinates[j][0][1]
        ):
            continue
        if (
            4 not in coordinates[j][1]
            and coordinates[i][0][0] < coordinates[j][0][0]
            and coordinates[i][0][1] > coordinates[j][0][1]
        ):
            continue

        point_inside = False

        for k in range(0, len(coordinates)):

            # There is a point k inside the area delimited by points i,j.
            if (
                coordinates[i][0][0] < coordinates[k][0][0] < coordinates[j][0][0]
                or coordinates[i][0][0] > coordinates[k][0][0] > coordinates[j][0][0]
            ) and (
                coordinates[i][0][1] < coordinates[k][0][1] < coordinates[j][0][1]
                or coordinates[i][0][1] > coordinates[k][0][1] > coordinates[j][0][1]
            ):
                point_inside = True
                break
            # There is a borderline inside the area delimited by points i,j. Edge cases are the borderlines created by i and j if they are adjacent.
            if (
                doIntersect(
                    [coordinates[i][0], coordinates[j][0]],
                    [coordinates[k - 1][0], coordinates[k][0]],
                )
                and k != i
                and k != j
                and k - 1 != i
                and k - 1 != j
            ):
                point_inside = True
                break

        if not point_inside:
            area = calculateArea(coordinates[i][0], coordinates[j][0])
            if area > maximum_area:
                maximum_area = max(maximum_area, area)

print(maximum_area)
