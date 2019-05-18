from collections import deque


def evaluate_postfix(expr):
    """
    Function for evaluating postfix expressions

    :param expr: expression in postfix form
    :return: result of evaluated expression
    """

    total = expr.split()
    stack = []
    for i in range(len(total)):
        if total[i] == "+":
            counter = stack.pop() + stack.pop()
        elif total[i] == "-":
            counter = -stack.pop() + stack.pop()
        elif total[i] == "*":
            counter = stack.pop() * stack.pop()
        elif total[i] == "/":
            counter = 1 / stack.pop() * stack.pop()
        else:
            counter = int(total[i])
        stack.append(counter)
    return stack[0]


def hot_potato(namelist, k):
    """
    Game in which people throw a hot potato amongst eachother, each k-th player looses

    :param namelist: list of people
    :param k: criterium for the game over part
    """
    counter = 1
    queue = deque(namelist)
    while len(queue) > 1:
        student = queue.popleft()
        queue.append(student)
        counter += 1
        if counter == k:
            stud = queue.popleft()
            print(queue, "student:", stud)
            counter = 0


def frequency_of_words(wordlist):
    """
    Function which prints the frequencies of each word in an input text
    :param wordlist:
    """
    frequency = {}
    w = wordlist.split()
    for word in w:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        print(words, frequency[words])
