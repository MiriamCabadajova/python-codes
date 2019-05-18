from random import randint


def guess_number_pc(upper_bound):
    number = int(input("Zadej cislo: "))
    lower_bound = 0
    middle = (lower_bound + upper_bound) // 2
    i = 1
    while lower_bound <= upper_bound:
        print("attempt number ", i)
        if number < middle:
            upper_bound = middle
            print("guess:", middle)
            print("my number is smaller")
        elif number > middle:
            lower_bound = middle
            print("guess:", lower_bound)
            print("my number is bigger")
        if middle == number:
            print("tip", middle)
            print("you guessed it")
            return
        middle = (upper_bound + lower_bound) // 2
        i += 1


def guess_number_human(upper_bound):
    number = randint(1, upper_bound)
    guess = 0
    while guess != number:
        guess = int(input("Guess the number:"))
        if guess > number:
            print("my number is smaller")
        elif guess < number:
            print("my number is bigger")
        elif guess == number:
            print("you guessed it")
            return
