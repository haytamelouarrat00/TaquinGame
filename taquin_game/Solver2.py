from queue import Queue
from taquin_base_game import *


def matrix_to_tuple(matrix):
    return tuple(tuple(row) for row in matrix)


def tuple_to_matrix(matrix_tuple):
    return [list(row) for row in matrix_tuple]


def bfs_solve(start_matrix):
    target = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    visited = set()
    queue = Queue()
    queue.put((start_matrix, []))

    while not queue.empty():
        current_matrix, path = queue.get()
        if matrix_to_tuple(current_matrix) == target:
            return path

        visited.add(matrix_to_tuple(current_matrix))
        empty_pos = get_elt(current_matrix, 9)[0]

        for row in range(3):
            for col in range(3):
                if are_adjacent(empty_pos[0], empty_pos[1], row, col):
                    new_matrix, _, _ = move_elt([r[:] for r in current_matrix], empty_pos[0], empty_pos[1], row, col, 0)
                    new_matrix_tuple = matrix_to_tuple(new_matrix)

                    if new_matrix_tuple not in visited:
                        new_path = path + [(row, col)]
                        queue.put((new_matrix, new_path))

    return None  # In case no solution is found


def ai_game2():
    matrix = create_table(3, 3)
    print("Initial Puzzle:")
    print_table(matrix)

    solution = bfs_solve(matrix)
    if solution:
        print("Solving...")
        for move in solution:
            matrix, _, _ = move_elt(matrix, get_elt(matrix, 9)[0][0], get_elt(matrix, 9)[0][1], move[0], move[1], 0)
            print_table(matrix)
            print("Move: ", move)
        print("Puzzle Solved in {} moves!".format(len(solution)))
    else:
        print("No solution found.")
