# Name: Andrew Osborne
# OSU Email: osborna2@oregonstate.edu
# Course: CS325
# Assignment: 7
# Due Date: 8/7/2022
# Description: An exploration of traveling salesman problems
from typing import List


def solve_tsp(G) -> List:
    """
    Takes as input an adjacency matrix and outputs a solution using the nearest
    neighbor heuristic.

    Sample input:
        G = [
        [0, 2, 3, 20, 1],
        [2, 0, 15, 2, 20],
        [3, 15, 0, 20, 13],
        [20, 2, 20, 0, 9],
        [1, 20, 13, 9, 0],
        ]

    Sample output (For above graph G):
        [0, 4, 3, 1, 2, 0]
    """

    solution = []

    # pick a random starting index
    random_start = 0
    solution.append(random_start)

    i = random_start
    while len(solution) < len(G):
        v = G[i]
        # set min_val and min_idx to absurd values
        min_val = max(v) + 1
        min_idx = min_val
        # implement nearest neighbor heuristic
        for e in range(len(v)):
            if v[e] == 0:
                pass
            elif v[e] <= min_val and e not in solution:
                min_val = v[e]
                min_idx = e
        solution.append(min_idx)
        i = min_idx
    # complete the cycle by addending the starting value
    solution.append(random_start)

    return solution


# input = [
#         [0, 2, 3, 20, 1],
#         [2, 0, 15, 2, 20],
#         [3, 15, 0, 20, 13],
#         [20, 2, 20, 0, 9],
#         [1, 20, 13, 9, 0],
#         ]
#
# result = solve_tsp(input)
# print(result)