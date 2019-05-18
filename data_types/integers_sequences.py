def fibonacci(n):
    """
    Implementation of fibonacci sequence
    :param n: number of elements of sequence to be printed
    """
    counter = 0
    a = 0
    b = 1
    while counter < n:
        c = a + b
        print(c, end=" ")
        counter += 1
        b = a
        a = c


def divisors_count(n):
    """
    Function which counts the number of divisors of n
    :param n: integer
    :return: number of divisors
    """
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return counter


def is_prime(n):
    """
    Function which tells whether a number is prime
    :param n: integer
    """
    return divisors_count(n) == 2


def primes(n):
    """
    Function which prints first n primes
    :param n: integer, number of primes
    """
    counter = 0
    i = 1
    while counter < n:
        if is_prime(i):
            print(i, end=" ")
            counter += 1
        i += 1


def arithmetic(base, d, n):
    """
    Implementation of arithmetic sum
    :param base: base element
    :param d: difference
    :param n: number of elements
    """
    for i in range(n):
        print(base, end=" ")
        base = base + d


def geometric(base, q, n):
    """
    Implementation of geometric sum
    :param base: base element
    :param q: quotient
    :param n: number of elements
    """
    for i in range(n):
        print(base, end=" ")
        base = base * q


def divisors(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    print(counter)


def hcd(n):
    """
    Function which finds the highest divisor of n smaller than n
    :param n: integer
    :return: highest divisor
    """
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if d < i < n:
                d = i
    return d


def digit_sum(n):
    """
    Function which calculates the digit sum of a number
    :param n: integer
    :return: digit sum of n
    """
    result = 0
    while n > 0:
        result += n % 10
        n = n // 10
    return result


def factorial(n):
    """
    Iterative version of factorial
    :param n: integer
    :return: factorial of n
    """
    f = 1
    for i in range(1, n + 1):
        f = i * f
    return f


def smallest_prime(n):
    """
    Function which prints smallest prime closest to n
    :param n: integer
    """
    i = n + 1
    counter = 0
    while n > 0 and counter < 1:
        if is_prime(i):
            print(i)
            counter += 1
        i += 1


def is_poweroftwo(n):
    """
    Function which tells whether a number is a power of two
    :param n: integer
    :return: true / false
    """
    i = 1
    b = 0
    while i < n:
        b = i * i
        if b == n:
            return True
        i += 1
    if b != n:
        return False


def is_sum_of_powers(n):
    """
    Function which tells whether a number is sum of two powers
    :param n: integer
    :return: true / false
    """
    b = 0
    for i in range(n):
        for j in range(n):
            b = i ** 2 + j ** 2
            if b == n:
                return True
    if b != n:
        return False


def binary(n):
    """
    Function which prints number in binary system
    :param n: integer
    """
    output = ""
    while n > 0:
        if n % 2 == 0:
            output = "0" + output
        else:
            output = "1" + output
        n = n // 2
    print(output)


def hexadecimal(n):
    """
    Function which prints number in hexadecimal system
    :param n: integer
    """
    if n < 0:
        print("0")
    elif n <= 1:
        print(n)
    else:
        hexadecimal(n // 16)
        x = (n % 16)
        if x < 10:
            print(x)
        if x == 10:
            print("A")
        if x == 11:
            print("B")
        if x == 12:
            print("C")
        if x == 13:
            print("D")
        if x == 14:
            print("E")
        if x == 15:
            print("F")


def information(a, b):
    """
    Function which gives various information about two numbers
    :param a: first number
    :param b: second number
    """
    n = 0
    counter = 0
    highest = 0
    primes_count = 0
    j = 0
    if a > b:
        n = a
        c = a - b
        print("Prve je vacsie o", c)
        for i in range(b, a):
            if is_prime(i):
                primes_count += 1
            if i == j * j:
                print("druhe mocniny:", i, end=" ")
            j += 1
        print("medzi", a, "a", b, "je", primes_count, "prvocisel")

    elif a < b:
        n = b
        c = b - a
        print("Druhe je vacsie o", c)
        for i in range(a, b):
            if is_prime(i):
                primes_count += 1
            if i == j * j:
                print("druhe mocniny:", i)
            j += 1
        print("medzi", a, "a", b, "je", primes_count, "prvocisel")

    if a % b == 0:
        print("Druhe deli prve")
    elif b % a == 0:
        print("Prve deli druhe")
    for i in range(1, n + 1):
        if a % i == 0 and b % i == 0:
            highest = i
            counter += 1
    print("Maju", counter, "spolocnych delitelov a najvacsi je", highest)


def lcm(a, b):
    """
    Function which finds least common multiple of two numbers
    :param a: first number
    :param b: second number
    :return: the least common multiple of two numbers
    """
    if a > b:
        a, b = b, a
    for i in range(b, a * b + 1, b):
        if i % a == 0:
            return i


def second_powers_in_interval(a, b):
    """
    Function which prints second powers in a given interval
    :param a: lower boundary
    :param b: upper boundary
    """
    mocniny = 1
    if a < mocniny < b:
        for i in range(a + 1, b):
            print(mocniny, end=" ")
            mocniny = i * i
    elif mocniny < a:
        for i in range(mocniny, b):
            print(mocniny, end=" ")
            mocniny = i * i
