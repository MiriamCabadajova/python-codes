from random import randint


def maxi(a):
    if len(a) == 1:
        return a[0]
    else:
        m = maxi(a[1:])
        if m > a[0]:
            return m
        else:
            return a[0]


def maximums(a):
    m = 0
    w = []
    for i in range(len(a)):
        b = maxi(a[i])
        w.append(b)
    return w


def rec_odd_sum(a):
    if len(a) == 0:
        return 0
    elif a[0] % 2 == 1:
        return a[0] + rec_odd_sum(a[1:])
    else:
        return rec_odd_sum(a[1:])


def d_20(n):
    f = {}
    counter = 0
    w = []
    avg = 0
    while counter < n:
        a = randint(1, 20)
        counter += 1
        avg += a
        f[a] = f.get(a, 0) + 1
    print("average:", avg / len(f))

    for number in sorted(f, key=f.get, reverse=True):
        print("most common value:", number)
        break

    for number in sorted(f, key=f.get, reverse=True):
        if f[number] == 1:
            print("the least common value:", number)
            break

    for number in sorted(f, key=f.get, reverse=True):
        if f[number] == 1:
            if number not in w:
                w.append(number)
    print("different values:", len(w))


def n_gram(s, n):
    a = []
    i = 0
    w = n
    f = {}
    while i < len(s):
        a.append(s[i:w])
        i += 1
        w += 1
    for word in a:
        f[word] = f.get(word, 0) + 1
    for word in sorted(f, key=f.get, reverse=True):
        if len(word) == n:
            print(word, f[word])


class Song:
    def __init__(self, name, genre, rating):
        self.name = name  # retezec
        self.genre = genre  # retezec
        self.rating = rating  # cele cislo od 0 do 10


class Band:
    def __init__(self, name, songs):
        self.name = name  # retezec
        self.songs = songs  # seznam prvku typu Song


def best_song_of_band(band):
    f = {}
    band.songs = sorted(band.songs, key=lambda x: (x.rating, x.name))
    for song in band.songs:
        f[song] = song
    return f[song]


def band_genres(band):
    w = []
    a = [song.genre for song in band.songs]
    a = sorted(a, key=lambda x: x)
    for i in range(len(a)):
        if a[i] not in w:
            w.append(a[i])
    return w


def average_of_songs_of_a_band(band):
    avg = 0
    for song in band.songs:
        avg += song.rating
    return avg / len(band.songs)


def best_bands(bands):
    f = {}
    a = []
    w = []
    for band in bands:
        a.append(average_of_songs_of_a_band(band))
        f[band] = average_of_songs_of_a_band(band)
    a = sorted(a, reverse=True)
    for band in bands:
        if f[band] == a[0]:
            w.append(band.name)
    w = sorted(w, key=lambda x: x)
    return w
