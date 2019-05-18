test_text = "it is a period of civil war and Rebel space strike to do a"


def is_word_char(char):
    """
    Checks whether character is one if the allowed symbols
    :param char: character
    :return: true / false
    """
    return char not in '!"#$%&\’()*+,-./:;<=>?@[\\]^_‘{}'


def word_freq(text):
    """
    Function which counts frequencies for each word
    :param text: string
    :return: dictionary of word frequency
    """
    text = "".join(filter(is_word_char, text))
    text = text.lower()
    word_list = text.split()
    freq = {}
    for word in word_list:
        freq[word] = freq.get(word, 0) + 1
    return freq


def output_for_freq(text):
    """
    Function which counts the word frequency and prints it out
    :param text: input string
    """
    freq = word_freq(text)
    for word in freq:
        print(word, "\t", freq[word])


def word_freq_file(filename="text.txt"):
    """
    Function which calculates the word frequencies from a file and then prints it
    :param filename: file
    """
    f = open(filename)
    text = ""
    for line in f.readlines():
        text += line
    output_for_freq(text)
    f.close()


def new_file(filename):
    file = open(filename, "w")
    file.write("Hello world! \n")
    file.write("This is the second line. \n")
    file.write("If you are wondering, this is how the third line looks like.")
    file.close()


def read_file(filename):
    """
    Function which reads lines from file
    :param filename: file
    :return: string representation of lines
    """
    f = open(filename)
    lines = f.read().splitlines()
    return lines


def process_team_line(line, teams):
    """
    Function which processes lines - strings
    :param line: string
    :param teams: array of strings
    :return: modifies parameter teams
    """
    team = line.split(":")
    for name in range(0):
        teams[name] = team[1].split(",")
        break
    members = team[1].split(",")
    return teams


def analyze_teams(filename):
    """
    Function which processes entire teams from a file
    :param filename: file
    """
    teams = {}
    lines = read_file(filename)
    for line in lines:
        process_team_line(line, teams)


morse = {"A": ".-", "B": "-...", "C": "-.-."}


def to_morse(text):
    """
    Function which converts text to morse
    :param text: string
    :return: string in morse
    """
    result = ""
    for c in text:
        result += morse.get(c, "?") + "|"
    return result