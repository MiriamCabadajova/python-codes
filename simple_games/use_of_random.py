from random import random, randint


def turn():
    """
    Function which prints numbers while even numbers are found
    :return:
    """
    odd_number = 2
    counter = 0
    while odd_number % 2 != 1:
        odd_number = randint(1, 6)
        counter += odd_number
        print(odd_number)
    return counter


def dice_stat(count, lower, upper):
    """
    Prints the statistics of rolling a dice count times
    :param count: number of rolls
    :param lower: the smallest number rolled
    :param upper: the largest number rolled
    """
    low = upper
    high = lower
    avg = 0

    for i in range(count):
        number = randint(lower, upper)

        if low > number:
            low = number

        if high < number:
            high = number

        avg += number

    print(low, high, avg / count)


def dice_freq(count):
    """
    Rolls the dice count times and prints the statistics for each number
    :param count: number of rolls
    """
    array = [0 for _ in range(6)]

    for i in range(count):
        number = randint(1, 6)
        array[number - 1] += 1

    return array


def two_dice_freq(count):
    """
    Rolls two dice count times and prints the statistics for each number
    :param count: number of rolls
    """
    array = [0 for _ in range(12)]

    for i in range(count):
        num_1 = randint(1, 6)
        num_2 = randint(1, 6)
        array[num_1 + num_2 - 1] += 1

    return array


def coin_flip():
    return True if randint(0, 100) <= 84 else False


def random_position():
    return 1 if randint(0, 1) == 1 else -1


def drunkman_simulator(size, steps):
    """
    Function for simulation of drunkman going home from bar
    :param size: the size of the route
    :param steps: number of steps he is going to make
    """
    position = size // 2
    for i in range(steps):
        print("home" + (position - 1) * '.' + '*' + (size - position) * '.' + "pub")
        position += int(random_position())
        if position == 0:
            print("home" + size * "." + "pub")
            print("drunkman arrived home")
            break
        if position == (size + 1):
            print("home" + size * "." + "pub")
            print("drunkman is at the pub again")
            break
        if i == steps:
            print("drunkman fell asleep")

# drunkman_simulator(5, 17)
