print("""---------
|       |
|       |
|       |
---------""")

grid = [[1, 1], [1, 2], [1, 3],
        [2, 1], [2, 2], [2, 3],
        [3, 1], [3, 2], [3, 3]]

symbols = list(" " * 9)

x_turn = True


def check_win(player):
    # check horizontal
    for row in range(0, 9, 3):
        if all(symbols[col] == player for col in range(row, row + 3)):
            return True

    # check vertical
    for col in range(3):
        if all(symbols[col] == player for col in range(col, col + 7, 3)):
            return True

    # check diagonals
    diagonals = [[symbols[0], symbols[4], symbols[8]],
                 [symbols[2], symbols[4], symbols[6]]]

    if any(i.count(player) == 3 for i in diagonals):
        return True

    return False


# check if game is draw - no side has 3 in a row and grid has no empty cells
def check_draw():
    draw = False

    if "_" not in symbols:
        draw = not check_win("X") and not check_win("O") and symbols.count(" ") == 0

    return draw


# check if game is impossible - grid has 3 Xs AND 3 Os OR more Xs than Os (vice versa)
def check_impossible():
    difference = abs(symbols.count("X") - symbols.count("O"))
    # impossible -- *does not include 3 X's and O's in a row*
    return check_win("X") and check_win("O") or difference >= 2 or \
        not check_win("X") and not check_win("O") and difference >= 2


# check if game finished - true = not finished
def check_game_not_finished():
    count = symbols.count(" ")
    # neither side has 3 in a row + still has empty cells
    # Falsy
    return not check_win("X") and not check_win("O") and count > 1


# check the index of the user_coordinate
def index_of_coordinate(coordinate, grid):
    # check if cell occupied
    for cell in grid:
        if cell == coordinate:
            # place the index that matches into i
            return grid.index(cell)


def is_cell_occupied(coordinate, grid, symbols):
    # check if cell occupied
    for cell in grid:

        if cell == coordinate:
            # place the index that matches into i
            index = index_of_coordinate(coordinate, grid)

            if symbols[index] == "X" or symbols[index] == "O":
                return True
            else:
                return False


# -------------------------------------------------------------------------------------------------------------------- #
while True:

    user_coordinate = input().split(" ")


    # analyze if move is correct:
    # check if input is numeric
    if not all([i.isnumeric() for i in user_coordinate]):
        print("You should enter numbers!")
        continue

    # convert to int type and put into list
    coordinate = [int(i) for i in list(user_coordinate)]

    # check if input is 1-3
    if not all([j in [1, 2, 3] for j in coordinate]):
        print("Coordinates should be from 1 to 3!")
        continue

    # check if cell is occupied
    coordinate_index = index_of_coordinate(coordinate, grid)

    if is_cell_occupied(coordinate, grid, symbols):
        print("This cell is occupied! Choose another one!")
        continue

    symbols[coordinate_index] = "X" if x_turn else "O"

    print("---------")
    print("| " + str(' '.join(symbols[:3])) + " |")
    print("| " + str(' '.join(symbols[3:6])) + " |")
    print("| " + str(' '.join(symbols[6:])) + " |")
    print("---------")

    # check game result
    if check_draw():
        print("Draw")
        break
    elif check_win("X"):
        print("X wins")
        break
    elif check_win("O"):
        print("O wins")
        break

    # switch turn
    x_turn = not x_turn
