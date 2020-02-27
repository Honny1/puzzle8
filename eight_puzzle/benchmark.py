from .puzzle import Puzzle
import time

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]]

cases = {
    "worst_case": [
        [8, 7, 6],
        [5, 4, 3],
        [2, 1, 0]
    ],
    "initial_state": [
        [1, 2, 5],
        [6, 8, 0],
        [7, 4, 3]
    ],
    "example_state0": [
        [1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]
    ],
    "example_state": [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ],
    "example_state1": [
        [1, 2, 7],
        [4, 5, 6],
        [3, 8, 0]
    ],
    "example_state2": [
        [1, 2, 4],
        [3, 5, 6],
        [7, 8, 0]
    ],
    "example_state3": [
        [8, 2, 3],
        [4, 5, 6],
        [7, 0, 1]
    ],
    "example_state4": [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ],
    "example_state5": [
        [1, 2, 3],
        [8, 0, 4],
        [7, 5, 6]
    ],
    "example_state6": [
        [1, 2, 3],
        [6, 4, 0],
        [7, 8, 5]
    ],
    "example_state7": [
        [8, 7, 6],
        [5, 4, 3],
        [2, 1, 0]
    ],
    "example_state8": [
        [1, 2, 3],
        [0, 5, 6],
        [4, 7, 8]
    ],
    "example_state9": [
        [2, 6, 0],
        [8, 1, 5],
        [4, 7, 3]
    ],
    "example_state10": [
        [0, 1, 3],
        [4, 2, 5],
        [7, 8, 6]
    ],
}

for case in cases:
    start_time = time.time()
    print(case)
    puzzle = Puzzle(cases[case], goal)
    moves = puzzle.process()
    print("--- %s seconds ---" % (time.time() - start_time))
    if moves:
        print(moves)