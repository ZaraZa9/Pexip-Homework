from solution import WordSearch
import random
import string


words_to_find = ["example", "aaaaaaaa"]


grid = []
for x in range(WordSearch.ROW_LENGTH):
    row = []
    for y in range(WordSearch.ROW_LENGTH):
        row.append(random.choice(string.ascii_lowercase))
    grid.append(row)


def add_word_horizontal(word):
    row = random.randint(0, WordSearch.ROW_LENGTH - 1)
    col = random.randint(0, WordSearch.ROW_LENGTH - len(word))
    for i in range(len(word)):
        grid[row][col + i] = word[i]

def add_word_vertical(word):
    row = random.randint(0, WordSearch.ROW_LENGTH - len(word))
    col = random.randint(0, WordSearch.ROW_LENGTH - 1)
    for i in range(len(word)):
        grid[row + i][col] = word[i]


words_to_place = words_to_find[:]
while len(words_to_place) > 0:
    word = random.choice(words_to_place)
    if random.choice([True, False]):
        add_word_horizontal(word)
    else:
        add_word_vertical(word)
    words_to_place.remove(word)


test_case = ''.join([''.join(row) for row in grid])

#running the test
ws = WordSearch(test_case)
for word in words_to_find:
    if ws.is_present(word):
        print("found {}".format(word))
    else:
        print("not found {}".format(word))