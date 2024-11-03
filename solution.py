import numpy as np

class WordSearch(object):
    ROW_LENGTH = 30
    rows = []
    columns = []

    def __init__(self, grid):

        arr = np.array(list(grid))
        self.grid = arr.reshape(self.ROW_LENGTH, self.ROW_LENGTH)


        for i in range(self.ROW_LENGTH):
            self.rows.append(''.join(self.grid[i, :]))
            self.columns.append(''.join(self.grid[:, i]))

        pass

    def is_present(self, word):
        for i in range(self.ROW_LENGTH):
            if word in self.rows[i] or word in self.columns[i]:
                return True
        return False


