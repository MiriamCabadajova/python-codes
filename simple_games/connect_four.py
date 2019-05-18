from random import randint

columns = int(input("Number of columns: "))
rows = int(input("Number of rows: "))


def empty_plan():
    p = []
    for i in range(rows):
        f = []
        for j in range(columns):
            f.append(0)
        p.append(f)
    return p


def print_board(state):
    symbol = {0: ".", 1: "X", 2: "O"}
    for i in range(rows):
        for j in range(columns):
            print(symbol[state[i][j]], end=" ")
        print()
    for i in range(columns):
        print("-", end=" ")
    print()
    for i in range(columns):
        print(i + 1, end=" ")
    print()


def check_for_row(s, i, j):  # -
    return s[i][j] == s[i + 1][j] == s[i + 2][j] == s[i + 3][j] != 0


def check_for_column(s, i, j):  # |
    return s[i][j] == s[i][j + 1] == s[i][j + 2] == s[i][j + 3] != 0


def check_for_diagonal(s, i, j):  # /
    return s[i][j] == s[i - 1][j + 1] == s[i - 2][j + 2] == s[i - 3][j + 3] != 0


def check_for_diagonal2(s, i, j):  # \
    return s[i][j] == s[i + 1][j + 1] == s[i + 2][j + 2] == s[i + 3][j + 3] != 0


def check_win(state):
    for i in range(rows):
        for j in range(columns):
            if j + 3 < columns and check_for_column(state, i, j):
                return state[i][j]
            if i + 3 < rows and check_for_row(state, i, j):
                return state[i][j]
            if j + 3 < columns and check_for_diagonal(state, i, j):
                return state[i][j]
            if j + 3 < columns and i + 3 < rows and check_for_diagonal2(state, i, j):
                return state[i][j]
    return 0


def is_draw(state):
    for i in range(columns):
        if state[0][i] == 0:
            return False
    return True


state = empty_plan()


def play(rows, columns, player1="human", player2="human"):
    if player1 == "human" and player2 == "human":
        print_board(state)
        while check_win(state) == 0:
            human_play(state, 1)
            if is_draw(state):
                break
            if check_win(state) == 0:
                human_play(state, 2)
        print("**Player", str(check_win(state)), "wins**")

    if player1 == "human" and player2 == "computer":
        print_board(state)
        while check_win(state) == 0:
            human_play(state, 1)
            if is_draw(state):
                break
            if check_win(state) == 0:
                computer_play(state, 2)
        print("**Player", str(check_win(state)), "wins**")

    if player1 == "computer" and player2 == "human":
        while check_win(state) == 0:
            computer_play(state, 1)
            if is_draw(state):
                break
            if check_win(state) == 0:
                human_play(state, 2)
        print("**Player", str(check_win(state)), "wins**")
        
    if player1 == "computer" and player2 == "computer":
        while check_win(state) == 0:
            computer_play(state, 1)
            if is_draw(state):
                break
            if check_win(state) == 0:
                computer_play(state, 2)
        print("**Player", str(check_win(state)), "wins**")


def human_play(state, number):
    print()
    print("Player", number)
    player = number
    move = int(input("Your move:"))
    for i in range(len(state)):
        if state[rows - 1 - i][move - 1] == 0:
            state[rows - 1 - i][move - 1] = player
            break
    print_board(state)


def computer_play(state, number):
    print()
    print("Player", number)
    player = number
    move = randint(1, columns)
    for i in range(len(state)):
        if state[rows - 1 - i][move - 1] == 0:
            state[rows - 1 - i][move - 1] = player
            break
    print_board(state)


play(rows, columns)
