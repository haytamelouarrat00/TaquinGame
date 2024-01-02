import random


def create_table(rows, cols):
    total_elements = rows * cols
    unique_random_numbers = random.sample(range(1, total_elements + 1), total_elements)
    return [unique_random_numbers[i:i + cols] for i in range(0, total_elements, cols)]


def are_adjacent(row1, col1, row2, col2):
    # Check if the elements share a common edge (horizontally or vertically)
    if abs(row1 - row2) == 1 and col1 == col2:
        return True
    elif abs(col1 - col2) == 1 and row1 == row2:
        return True
    else:
        return False


def move_elt(matrix, io, jo, id, jd, iteration):  # io, jo original coordinates of elt to move, id, jd destination
    if are_adjacent(io, jo, id, jd):
        matrix[io][jo], matrix[id][jd] = matrix[id][jd], matrix[io][jo]
        iteration += 1
        return matrix, 1, iteration
    else:
        return matrix, 0, iteration


def print_table(matrix):
    for row in matrix:
        modified_row = [str(' ' if element == 9 else element) for element in row]
        print(modified_row)


def get_elt(matrix, elt):
    return [(index, row.index(elt)) for index, row in enumerate(matrix) if elt in row]


def read_user_input():
    input_str = input("Enter a tuple of integers (e.g., 1, 2, 3): ")
    input_values = input_str.split(',')
    try:
        int_tuple = tuple(map(int, input_values))
        print(f"Tuple of integers entered: {int_tuple}")
        return int_tuple
    except ValueError:
        print("Invalid input. Please enter a valid tuple of integers separated by commas.")


def read_input(matrix):
    input_str = int(input("Enter a number adjacent to the empty space: "))
    if 0 < input_str < 9:
        return get_elt(matrix, input_str)[0][0], get_elt(matrix, input_str)[0][1]


def is_matrix_sorted(matrix):
    # Check rows
    for row in matrix:
        if row != sorted(row):
            return False

    # Check columns
    for col in range(len(matrix[0])):
        column = [matrix[row][col] for row in range(len(matrix))]
        if column != sorted(column):
            return False

    return True


def game():
    i = 0
    matrix = create_table(3, 3)
    while not is_matrix_sorted(matrix):
        print_table(matrix)
        player_choice = read_input(matrix)
        matrix, check, i = move_elt(matrix, player_choice[0], player_choice[1],
                                    get_elt(matrix, 9)[0][0], get_elt(matrix, 9)[0][1], i)
        print("Move number: {0}".format(i))
        if not check:
            print("Sorry input invalid, try again!")
