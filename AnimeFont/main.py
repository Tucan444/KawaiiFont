import string
import pygame
import os

pygame.init()  # initiate pygame

pygame.display.set_caption('Pygame')  # set the window name

letter_height = 80
WINDOW_SIZE = (1, 0)  # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)  # initiate screen


def filter_text(text):
    t = list(map(lambda s: s.lower(), [s for s in text]))

    i_to_r = []
    for i, letter in enumerate(t):
        if letter not in string.ascii_lowercase + " ":
            i_to_r.append(i)

    load = 0
    for i in i_to_r:
        del t[i - load]
        load += 1

    return "".join(t)


def get_letters(letter_height, path=None):

    letters = {letter.split(".")[0]: pygame.image.load(path + letter).convert() for letter in os.listdir(path)
               if (letter.endswith(".png") or letter.endswith(".jpg")) and "-" not in letter}

    for key, letter in letters.items():
        s = letter.get_width() / letter.get_height()
        letters[key] = pygame.transform.scale(letters[key], (int(letter_height * s), letter_height))

    return letters


def get_word_length(word, letters):
    return sum([letters[letter].get_width() for letter in word])


def get_image(text, letters, letter_height, bg=(54, 57, 63)):
    text = filter_text(text)
    t = text.split(" ")
    word_lengths = list(map(lambda x: get_word_length(x, letters), t))
    max_length = max(word_lengths)
    if len(word_lengths) > 3:
        max_length *= 2
    lines = 1
    cl = 0
    i = 0

    # getting image size
    for w, l in zip(t, word_lengths):
        if cl + l > max_length:
            cl = l
            lines += 1
        else:
            cl += l

        if i != len(t) - 1:
            if cl + (letter_height * 0.5) > max_length:
                cl = 0
                lines += 1
            else:
                cl += (letter_height * 0.5)

        i += 1

    # creating surface
    sur = pygame.Surface((max_length, lines * letter_height))
    sur.fill(bg)

    # rendering text onto surface
    pos = [0, 0]
    i = 0
    for w, l in zip(t, word_lengths):
        if pos[0] + l > max_length:
            pos[0] = 0
            pos[1] += letter_height
            for letter in w:
                sur.blit(letters[letter], pos)
                pos[0] += letters[letter].get_width()

        else:
            for letter in w:
                sur.blit(letters[letter], pos)
                pos[0] += letters[letter].get_width()

        if i != len(t) - 1:
            if pos[0] + (letter_height * 0.5) > max_length:
                pos[0] = 0
                pos[1] += letter_height
            else:
                pos[0] += (letter_height * 0.5)

        i += 1

    return sur
