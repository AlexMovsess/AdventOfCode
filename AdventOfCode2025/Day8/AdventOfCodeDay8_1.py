import os
import numpy as np

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "AdventOfCodeDay8.txt")) as f:
    content = f.read()
    lines = content.split("\n")
    coordinates = [[int(x) for x in line.split(",")] for line in lines]


def calculate_distance(list1, list2):
    p1 = np.array(list1)
    p2 = np.array(list2)
    d = np.sqrt(np.sum((p1 - p2) ** 2))
    return d


distances = {}

for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        distances[(i, j)] = calculate_distance(coordinates[i], coordinates[j])

list_distances_sorted = [
    entry[0] for entry in sorted(distances.items(), key=lambda item: item[1])[:1000]
]

circuit_list = []

for i in range(len(list_distances_sorted)):
    connected_nodes = []
    for j in range(len(circuit_list)):

        if (
            list_distances_sorted[i][0] in circuit_list[j]
            or list_distances_sorted[i][1] in circuit_list[j]
        ):
            connected_nodes.append(j)

    if not connected_nodes:
        circuit_list.append(set(list_distances_sorted[i]))

    else:
        new_circuit = set(list_distances_sorted[i])

        for j in connected_nodes:

            new_circuit.update(set(circuit_list[j]))
            circuit_list[j] = (
                {}
            )  # Can't remove it because we are iterating over the list, can't replace it because there might be several occurences. Replacing with empty set is not very pretty but it works.

        circuit_list.append(new_circuit)

top3_circuits = sorted(circuit_list, key=lambda item: len(item), reverse=True)[:3]

print(len(top3_circuits[0]) * len(top3_circuits[1]) * len(top3_circuits[2]))
