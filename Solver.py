import heapq
import itertools

from taquin_base_game import *


# The existing functions (create_table, are_adjacent, move_elt, print_table, get_elt, read_user_input, read_input, is_matrix_sorted) remain the same

def manhattan_distance(matrix, target=9):
    total_distance = 0
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == target:
                continue
            target_x, target_y = divmod(value - 1, len(matrix[0]))
            total_distance += abs(target_x - i) + abs(target_y - j)
    return total_distance


def get_possible_moves(matrix):
    moves = []
    x, y = get_elt(matrix, 9)[0]
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
            moves.append((nx, ny))
    return moves


def convert_to_flat(matrix):
    if isinstance(matrix, list) and all(isinstance(row, list) for row in matrix):
        return tuple(itertools.chain(*matrix))
    print("Error: Invalid matrix structure passed to convert_to_flat:", matrix)
    raise ValueError("Input must be a 2D matrix")


def convert_to_matrix(flat, rows, cols):
    return [list(flat[i * cols:(i + 1) * cols]) for i in range(rows)]


def a_star_solver(matrix):
    rows, cols = len(matrix), len(matrix[0])
    goal = convert_to_flat([sorted(range(1, rows * cols)) + [9]])
    queue = [(manhattan_distance(matrix), 0, convert_to_flat(matrix), [])]
    seen = set()

    while queue:
        _, cost, current_flat, path = heapq.heappop(queue)
        current_matrix = convert_to_matrix(current_flat, rows, cols)

        if current_flat == goal:
            return path

        if current_flat in seen:
            continue
        seen.add(current_flat)

        x, y = get_elt(current_matrix, 9)[0]
        for move in get_possible_moves(current_matrix):
            new_matrix = [row[:] for row in current_matrix]
            new_matrix[x][y], new_matrix[move[0]][move[1]] = new_matrix[move[0]][move[1]], new_matrix[x][y]
            new_cost = cost + 1
            new_flat = convert_to_flat(new_matrix)
            heapq.heappush(queue, (new_cost + manhattan_distance(new_matrix), new_cost, new_flat, path + [move]))

    return []


def count_inversions(sequence):
    inversions = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j] and sequence[i] != 9 and sequence[j] != 9:
                inversions += 1
    return inversions


def is_solvable(matrix):
    flat_matrix = convert_to_flat(matrix)
    return count_inversions(flat_matrix) % 2 == 0


def ai_game():
    matrix = create_table(3, 3)
    while not is_solvable(matrix):
        matrix = create_table(3, 3)

    print("Initial State:")
    print_table(matrix)

    while not is_matrix_sorted(matrix):
        if input("Press 'A' for AI to solve, or any other key to continue: ").lower() == 'a':
            for move in a_star_solver(matrix):
                print("AI Move: ", move)
                matrix, _, _ = move_elt(matrix, *get_elt(matrix, 9)[0], *move, 0)
                print_table(matrix)
            break
        else:
            player_choice = read_input(matrix)
            matrix, _, _ = move_elt(matrix, *player_choice, *get_elt(matrix, 9)[0], 0)
            print_table(matrix)
