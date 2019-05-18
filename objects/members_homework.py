# 40
class Person:
    """Represents a member of the association.
    Attributes:
        name: string
        year_of_birth: int
        degree: one of 'bc', 'mgr', 'phd'
        mentor: another Person who is the mentor of this person
        mentees: list of Persons, direct mentees of this person
    """

    def __init__(self, name, year_of_birth, degree):
        """Initialize new Person object.
        >>> martin = Person('Martin', 1991, 'phd')
        >>> martin.name
        'Martin'
        >>> martin.year_of_birth
        1991
        >>> martin.degree
        'phd'
        """
        self.name = name
        self.year_of_birth = int(year_of_birth)
        self.degree = degree
        self.mentor = None
        self.mentees = []

    def describe(self):
        """Return string representation of this person.
        >>> martin = Person('Martin', 1991, 'phd')
        >>> martin.describe()
        'Martin (1991)'
        """
        return str(self.name) + " (" + str(self.year_of_birth) + ")"


class Team:
    """Represents a group of people working together on one event.
    Attributes:
        name: string, name of the event
        members: list of Persons working on this event
    """

    def __init__(self, name):
        """Initialize new Team object.
        >>> team = Team('InterJeLen')
        >>> team.name
        'InterJeLen'
        >>> team.members
        []
        """
        self.name = name
        self.members = []

    def add_member(self, member):
        """Add new member to this team.
        >>> team = Team('InterJeLen')
        >>> dominika = Person('Dominika', 1995, 'bc')
        >>> team.add_member(dominika)
        >>> [member.name for member in team.members]
        ['Dominika']
        """
        self.members.append(member)


def create_mentorship(mentor, mentee):
    """Create new relationship between a mentor and a mentee.
    >>> martin = Person('Martin', 1991, 'phd')
    >>> tom = Person('Tom', 1993, 'mgr')
    >>> create_mentorship(martin, tom)
    >>> tom.mentor.name
    'Martin'
    >>> [mentee.name for mentee in martin.mentees]
    ['Tom']
    """
    mentor.mentees.append(mentee)
    mentee.mentor = mentor


def get_longest_name(people):
    """Return longest name among all people.
    Args:
        people: dictionary mapping names to Persons
    Returns:
        the longest name (string)
    >>> people = {}
    >>> people['martin'] = Person('Martin', 1991, 'phd')
    >>> people['honza'] = Person('Honza', 1995, 'bc')
    >>> get_longest_name(people)
    'Martin'
    """
    for person in sorted(people, key=lambda x: -len(people[x].name)):
        return people[person].name


def get_founder(people):
    """Return a person without a mentor.
    In the association, there should be only one person without a mentor, this
    person is called `founder`. This function finds and returns the founder.
    Args:
        people: dictionary mapping names to Persons
    Returns:
        Person without a mentor
    >>> martin = Person('Martin', 1991, 'phd')
    >>> tom = Person('Tom', 1993, 'mgr')
    >>> create_mentorship(martin, tom)
    >>> people = {'martin': martin, 'tom': tom}
    >>> founder = get_founder(people)
    >>> founder.name
    'Martin'
    """
    for person in people:
        if people[person].mentor is None:
            return people[person]
        return get_founder(people[person].mentor)


def print_mentorship_tree(people):
    """Print tree of mentorship, see the example below.
    Indents each level by 2 spaces. Mentees of a mentor are ordered by names.
    Hint:
        Use `get_founder` and `print_mentorship_subtree` helper functions.
    Args:
        people: dictionary mapping names to Person objects
    >>> people = {}
    >>> people['Martin'] = Person('Martin', 1991, 'phd')
    >>> people['Lukas'] = Person('Lukas', 1991, 'phd')
    >>> people['Tom'] = Person('Tom', 1993, 'mgr')
    >>> people['Honza'] = Person('Honza', 1995, 'bc')
    >>> create_mentorship(people['Martin'], people['Tom'])
    >>> create_mentorship(people['Tom'], people['Honza'])
    >>> create_mentorship(people['Martin'], people['Lukas'])
    >>> print_mentorship_tree(people)
    Martin (1991)
      Lukas (1991)
      Tom (1993)
        Honza (1995)
    """
    founder = get_founder(people)
    print_mentorship_subtree(founder, level=0)


def print_mentorship_subtree(person, level=0):
    """Print person with all transitive mentees as a tree.
    Indents each level by 2 spaces. Mentees of a mentor are ordered by names.
    Args:
        person: Person at the root of the printed tree
        level: number of double-spaces to add before each printed line
               (level=0 for 0 space, level=1 for 2 spaces, etc.)
    >>> people = {}
    >>> people['tom'] = Person('Tom', 1993, 'mgr')
    >>> people['honza'] = Person('Honza', 1995, 'bc')
    >>> create_mentorship(people['tom'], people['honza'])
    >>> print_mentorship_subtree(people['tom'], level=1)
      Tom (1993)
        Honza (1995)
    """
    print(("  " * level) + person.name + " (" + str(person.year_of_birth) + ")")
    person.mentees = sorted(person.mentees, key=lambda x: x.name)
    for mentee in person.mentees:
        print_mentorship_subtree(mentee, level + 1)


def count_transitive_mentees(person):
    """Return number of transitive mentees of given person.
    Transitive mentees are all person's mentees, mentees of these mentees, etc.
    >>> martin = Person('Martin', 1991, 'phd')
    >>> lukas = Person('Lukas', 1991, 'phd')
    >>> tom = Person('Tom', 1993, 'mgr')
    >>> honza = Person('Honza', 1995, 'bc')
    >>> create_mentorship(martin, lukas)
    >>> create_mentorship(martin, tom)
    >>> create_mentorship(tom, honza)
    >>> count_transitive_mentees(martin)
    3
    >>> count_transitive_mentees(tom)
    1
    >>> count_transitive_mentees(honza)
    0
    """
    counter = 0
    for mentee in person.mentees:
        counter += 1 + count_transitive_mentees(mentee)
    return counter


def count_transitive_mentees_with_degree(person, degree):
    """Return number of transitive mentees who persue given degree.
    >>> martin = Person('Martin', 1991, 'phd')
    >>> tom = Person('Tom', 1993, 'mgr')
    >>> honza = Person('Honza', 1995, 'bc')
    >>> create_mentorship(martin, tom)
    >>> create_mentorship(tom, honza)
    >>> count_transitive_mentees_with_degree(martin, 'bc')
    1
    """
    counter = 0
    for mentee in person.mentees:
        if mentee.degree == degree:
            counter += 1 + count_transitive_mentees_with_degree(mentee, degree)
        else:
            counter += count_transitive_mentees_with_degree(mentee, degree)
    return counter


def get_transitive_mentors(person):
    """Return list with a person's mentor, mentor of this mentor, etc.
    >>> martin = Person('Martin', 1991, 'phd')
    >>> tom = Person('Tom', 1993, 'mgr')
    >>> honza = Person('Honza', 1995, 'bc')
    >>> create_mentorship(martin, tom)
    >>> create_mentorship(tom, honza)
    >>> [person.name for person in get_transitive_mentors(honza)]
    ['Tom', 'Martin']
    """
    s = []
    while person.mentor is not None:
        s.append(person.mentor)
        person = person.mentor
    return s


def get_person_with_most_mentees(people):
    """Return the person who has most mentees (counting direct mentees only).
    Args:
        people: dictionary mapping names to Persons
    >>> people = {}
    >>> people['Martin'] = Person('Martin', 1991, 'phd')
    >>> people['Lukas'] = Person('Lukas', 1991, 'phd')
    >>> people['Tom'] = Person('Tom', 1993, 'mgr')
    >>> people['Honza'] = Person('Honza', 1995, 'bc')
    >>> create_mentorship(people['Martin'], people['Lukas'])
    >>> create_mentorship(people['Martin'], people['Tom'])
    >>> create_mentorship(people['Tom'], people['Honza'])
    >>> get_person_with_most_mentees(people).name
    'Martin'
    """
    ppl = list(people.values())
    ppl = sorted(ppl, key=lambda x: -len(x.mentees))
    return ppl[0]


def get_team_year_of_birth_median(team):
    """Return median year of birth of team members.
    If the team has even number of members,
    return the smaller of the two years in the middle.
    >>> team = Team('InterJeLen')
    >>> team.add_member(Person('a', 1990, 'phd'))
    >>> team.add_member(Person('b', 1995, 'bc'))
    >>> team.add_member(Person('c', 1996, 'bc'))
    >>> get_team_year_of_birth_median(team)
    1995
    >>> team.add_member(Person('d', 1996, 'bc'))
    >>> get_team_year_of_birth_median(team)
    1995
    """
    a = [member.year_of_birth for member in team.members]
    if len(a) % 2 == 0:
        if a[len(a) // 2 - 1] > a[len(a) // 2]:
            return a[len(a) // 2]
        else:
            return a[len(a) // 2 - 1]
    else:
        return a[len(a) // 2]


def get_most_common_degree_in_team(team):
    """Return degree which occurs most times in the team.
    If there are multiple degrees which appears most times, return any of them.
    >>> team = Team('InterJeLen')
    >>> team.add_member(Person('a', 1990, 'phd'))
    >>> team.add_member(Person('b', 1995, 'bc'))
    >>> team.add_member(Person('c', 1996, 'bc'))
    >>> get_most_common_degree_in_team(team)
    'bc'
    """
    a = [member.degree for member in team.members]
    f = {}
    for degree in a:
        f[degree] = f.get(degree, 0) + 1
    f = sorted(f, key=f.get, reverse=True)
    return f[0]


def print_team_info(team):
    """Prints name, members, median year of birth and the most common degree.
    Members are printed from the oldest to the youngest.
    >>> team = Team('InterJeLen')
    >>> team.add_member(Person('Petra', 1995, 'bc'))
    >>> team.add_member(Person('Pavla', 1996, 'bc'))
    >>> team.add_member(Person('Matej', 1990, 'phd'))
    >>> print_team_info(team)
    ----------------
    Team: InterJeLen
    ----------------
    Matej (1990)
    Petra (1995)
    Pavla (1996)
    --
    median year of birth: 1995
    most common degree: bc
    """
    for i in range(len(team.name) + 6):
        print("-", end="")
    print()
    print("Team:", team.name)
    for i in range(len(team.name) + 6):
        print("-", end="")
    print()
    team.members = sorted(team.members, key=lambda x: x.year_of_birth)
    for person in team.members:
        print(person.describe())
    print("--")
    print("median year of birth:", get_team_year_of_birth_median(team))
    print("most common degree:", get_most_common_degree_in_team(team))


def print_all_teams_info(teams):
    """Print info about all given teams. Teams are ordered by names.
    >>> teams = {'x': Team('x'), 'y': Team('y')}
    >>> teams['x'].add_member(Person('a', 1995, 'bc'))
    >>> teams['y'].add_member(Person('b', 1996, 'bc'))
    >>> print_all_teams_info(teams)
    -------
    Team: x
    -------
    a (1995)
    --
    median year of birth: 1995
    most common degree: bc
    -------
    Team: y
    -------
    b (1996)
    --
    median year of birth: 1996
    most common degree: bc
    """
    teams = list(teams.values())
    teams = sorted(teams, key=lambda x: x.name)
    for i in range(len(teams)):
        print_team_info(teams[i])


def get_common_members_names(team1, team2):
    """Return set of persons' names that are members of both teams.
    Return:
        set of persons' names
    >>> intersob = Team('InterSoB')
    >>> interlos = Team('InterLoS')
    >>> a = Person('a', 1995, 'bc')
    >>> b = Person('b', 1995, 'bc')
    >>> c = Person('c', 1995, 'bc')
    >>> intersob.members = [a, b]
    >>> interlos.members = [b, c]
    >>> get_common_members_names(intersob, interlos)
    {'b'}
    """
    team1 = [member.name for member in team1.members]
    team2 = [member.name for member in team2.members]
    l = (set(team1) & set(team2))
    return l


def get_common_teams_names(person1, person2, teams):
    """Return set of teams (their names) in which are both persons.
    Args:
        person1: Person
        person2: Person
        teams: dictionary mapping team names to Team objects
    Return:
        set of teams' names
    >>> teams = {'x': Team('x'), 'y': Team('y'), 'z': Team('z')}
    >>> a = Person('a', 1995, 'bc')
    >>> b = Person('b', 1995, 'bc')
    >>> teams['x'].add_member(a)
    >>> teams['y'].add_member(a)
    >>> teams['y'].add_member(b)
    >>> teams['z'].add_member(b)
    >>> get_common_teams_names(a, b, teams)
    {'y'}
    """
    a = list(teams.values())
    f = {}
    i = 0
    result = []
    for person in a:
        f[person.name] = a[i].members
        i += 1
    for person in f:
        if person1 in f[person]:
            if person2 in f[person]:
                result.append(teams[person].name)
    return set(sorted(result))


def process_person_line(line, people):
    """Parse one line of input file containg info about a person.
    """
    name, year, degree = line.split(',')
    people[name] = Person(name, int(year), degree)


def process_mentor_line(line, people):
    """Parse one line of input file containg info about a mentorship.
    >>> petra = Person('Petra', 1993, 'mgr')
    >>> pavla = Person('Pavla', 1995, 'bc')
    >>> people = {'Petra': petra, 'Pavla': pavla}
    >>> process_mentor_line('Petra->Pavla', people)
    >>> pavla.mentor.name
    'Petra'
    >>> petra.mentees == [pavla]
    True
    """
    mentor, mentee = line.split("->")
    mentor = people[mentor]
    mentee = people[mentee]
    create_mentorship(mentor, mentee)


def process_team_line(line, people, teams):
    """Parse one line of input file containg info about a team.
    >>> petra = Person('Petra', 1995, 'bc')
    >>> pavla = Person('Pavla', 1995, 'bc')
    >>> people = {'Petra': petra, 'Pavla': pavla}
    >>> teams = {}
    >>> process_team_line('InterJeLen:Petra,Pavla', people, teams)
    >>> teams['InterJeLen'].members == [petra, pavla]
    True
    """
    team, members = line.split(":")
    members = members.split(",")

    for t in team:
        teams[team] = Team(team)
    for member in members:
        teams[team].add_member(people[member])


def read_file(filename):
    """Read file and return list of lines. Remove new lines.
    >>> lines = read_file('members.txt')
    >>> len(lines)
    34
    >>> lines[:3]
    ['=== People ===', 'Martin,1991,phd', 'Maara,1989,phd']
    """
    with open(filename, "r") as infile:
        text = infile.read().splitlines()
    return text


def read_data(filename='members.txt'):
    """Read and parse data in given filename; return people and teams.
    Function expects data in the same format as in example  'members.txt' file.
    No input data validation is performed.
    Return:
        (people, teams): dictionaries mapping names to Person/Team objects
    >>> people, teams = read_data()
    >>> len(people)
    14
    >>> people['Tyna'].describe()
    'Tyna (1993)'
    >>> len(teams)
    4
    >>> print_team_info(teams['InterSoB'])
    --------------
    Team: InterSoB
    --------------
    Lukas (1991)
    Tom (1993)
    Radka (1994)
    Dominika (1995)
    --
    median year of birth: 1993
    most common degree: mgr
    """
    people, teams = {}, {}
    lines = read_file(filename)
    mode = None  # current section of the file: 'people', 'mentors' or 'teams'
    for line in lines:
        if line == '=== People ===':
            mode = 'people'
        elif line == '=== Mentors ===':
            mode = 'mentors'
        elif line == '=== Teams ===':
            mode = 'teams'
        elif mode == 'people':
            process_person_line(line, people)
        elif mode == 'mentors':
            process_mentor_line(line, people)
        elif mode == 'teams':
            process_team_line(line, people, teams)
        else:
            raise ValueError('Invalid state when reading file.')
    return people, teams


def main():
    """Read data about members of the association and print some info.
    """
    people, teams = read_data()
    print('longest name:', get_longest_name(people))
    print('founder:', get_founder(people).name)
    print_mentorship_tree(people)
    print('transitive mentees of Lukas:',
          count_transitive_mentees(people['Lukas']))
    print('transitive mgr mentees of Lukas:',
          count_transitive_mentees_with_degree(people['Lukas'], 'mgr'))
    print('transitive mentors of Ondra:',
          [person.name for person in get_transitive_mentors(people['Ondra'])])
    print('person with most mentees:',
          get_person_with_most_mentees(people).name)
    print_all_teams_info(teams)
    print('common members of InterSoB and KSI:',
          get_common_members_names(teams['InterSoB'], teams['KSI']))
    print('common teams of Dominika and Vlada:',
          get_common_teams_names(people['Dominika'], people['Vlada'], teams))


def test():
    """Check examples in docstrings.
    If the actual output matches the expected output, doesn't print anything.
    Otherwise, it prints an error message showing the mismatch.
    """
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    # main()
    test()


def output(filename):
    people, teams = read_data()
    print("longest name:", get_longest_name(people))
    founder = get_founder(people)
    print("founder:", founder.name)
    print_mentorship_tree(people)
    print("transitive mentees of Lukas:",
          count_transitive_mentees(people["Lukas"]))
    print("transitive mgr mentees of Lukas:",
          count_transitive_mentees_with_degree(people["Lukas"], "mgr"))
    print("transitive mentors of Ondra:",
          [person.name for person in get_transitive_mentors(people["Ondra"])])
    print("person with most mentees:",
          get_person_with_most_mentees(people).name)
    print_all_teams_info(teams)
    print("common members of InterSoB and KSI:",
          get_common_members_names(teams["InterSoB"], teams["KSI"]))
    print("common teams of Dominika and Vlada",
          get_common_teams_names(people["Dominika"], people["Vlada"], teams))


output("members.txt")
