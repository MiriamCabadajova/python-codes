from random import randint


def game(length, n, k, output=True):
    new_position = 1
    if length < 2 or n <= 0:
        print("You are not allowed to play")
        return False
    turn = 0
    while new_position <= length:
        turn += 1
        r = randint(1, 6)
        if output:
            print("Turn:", turn, "=", r, end=" ")
        while r % 6 == 0:
            n = randint(1, 6)
            if output:
                print(n, end=" ")
            r += n
        new_position += r
        if new_position > length:
            new_position -= r
            if output:
                print("-> new position:", new_position)
        elif new_position <= length:
            if new_position == length:
                if output:
                    print("-> new position:", new_position)
                    print("Game ended at turn", end=" ")
                    return turn
                if not output:
                    return turn
            else:
                if new_position % n == 0:
                    if new_position - k < 0:
                        new_position = 0
                    else:
                        new_position -= k
                    if output:
                        print("-> new position:", new_position)
                else:
                    if output:
                        print("-> new position:", new_position)


def game_analysis(length, n, k, count):
    avg = 0
    r = 0
    for i in range(count):
        avg = game(length, n, k, False)
        r += avg
    return r / count


def game_average_length(count):
    hra = 0
    for length in range(10, 21):
        for n in range(2, 5):
            for k in range(1, 4):
                r = 0
                print("Length =", length, "; n =", n, "; k =", k, ": Average number of moves = ", end="")
                print(game_analysis(length, n, k, count))


# game(5, 2, 1)