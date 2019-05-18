import re
from PIL import Image


def to_words(text):
    text_without_interpuction = re.sub('[\W_]', ' ', text)
    words = text_without_interpuction.split()
    return words


def name_analysis(filename):
    with open(filename, "r") as infile:
        text = infile.read()
    text = to_words(text)
    result = {}
    for name in text:
        result[name[0]] = result.get(name[0], 0) + 1
    for name in sorted(result, key=result.get, reverse=True):
        print(name[0], ":", result[name[0]])


def graph_of_name_analysis(filename):
    with open(filename, "r") as infile:
        text = infile.read()
    text = to_words(text)
    result = {}
    i = 0
    for name in text:
        result[name[0]] = result.get(name[0], 0) + 1

    temp = result.copy()
    alist = sorted(result, key=result.get, reverse=True)

    if result[alist[0]] % 50 == 0:
        i = result[alist[0]]
    else:
        i = ((result[alist[0]] // 50) + 1) * 50
    while i > 0:
        a = str(i)
        print(a.rjust(3), end="")
        for letter in alist:
            if i - temp[letter] < temp[letter] - (i - 50):
                print("#", end="")
                temp[letter] -= 50
        print()
        i -= 50
    print("   ", end="")

    for letter in alist:
        print(letter, end="")


def list_of_names():
    with open("memb.txt", "r") as infile:
        text = infile.read()
    text = to_words(text)
    return text


def first_letter():
    allow = input("is the fist letter important for you? (yes/no): ")
    if allow == "yes":
        letter = input(str("which first letter do you prefer? "))
        letter = letter.upper()
    else:
        return set()
    alist = list_of_names()
    result = []
    for i in range(len(alist)):
        if alist[i][0] == letter:
            result.append(alist[i])
    return set(result)


def max_length():
    allow = input("is the length of the name important for you? (yes/no): ")
    if allow == "yes":
        length = input("what is the maximal length you would allow? ")
        length = int(length)
    else:
        return set()

    alist = list_of_names()
    result = []
    for i in range(len(alist)):
        if len(alist[i]) <= length:
            result.append(alist[i])
    if not result:
        print("*sorry but there are not such short names in our database*")
        return set(result)
    return set(result)


def vowels_in_name():
    allow = input("is the number of vowels important? (yes/no): ")
    if allow == "yes":
        number = int(input("maximum number of vowels: "))
    else:
        return set()
    alist = list_of_names()
    result = []
    f = {}
    vowels = "aeiouyAEIOUY"

    if number == 0:
        print("*sorry but there are no names without vowels in our database*")
        return set(result)

    for name in alist:
        for i in range(len(name)):
            if name[i] in vowels:
                f[name] = f.get(name, 0) + 1

    temp = sorted(f, key=f.get)
    for name in temp:
        if f[name] <= number:
            result.append(name)

    return set(result)


def find_name_for_your_child():
    temp = [first_letter(), max_length(), vowels_in_name()]
    set_list = []
    for s in temp:
        if len(s) != 0:
            set_list.append(s)

    if len(set_list) == 0:
        print("sorry but no name meets your requirements")
        return

    result = set_list[0]
    for s in set_list[1:]:
        result = result & s

    if len(result) == 0:
        print("sorry but no name meets your requirements")
    else:
        print()
        print("possible names:")
        for name in sorted(result, key=lambda x: x):
            print(name)


def combine(file1, file2):
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    image1 = image1.convert("RGBA")
    image2 = image2.convert("RGBA")

    result = Image.blend(image1, image2, alpha=.5)
    result.show()


def linear(x):
    return 0.5 * x


def hill(x):
    return (-1) * (x ** 2)
