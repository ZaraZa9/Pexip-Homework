import numpy as np

class WordSearch(object):
    ROW_LENGTH = 10000
    MAX_WORD_LENGTH = 24

    def __init__(self, grid):

        arr = np.array(list(grid))
        self.grid = arr.reshape(self.ROW_LENGTH, self.ROW_LENGTH)

    def is_present(self, word):
        word_len = len(word)
        
        for i in range(self.ROW_LENGTH):
            row = ''.join(self.grid[i, :])
            col = ''.join(self.grid[:, i])
            for j in range(self.ROW_LENGTH - word_len + 1):
                if (row[j:j + word_len] == word) or (col[j:j + word_len] == word):
                    return True


        return False
