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


            while True:
                #get indexes of the first letter of the word in the row and column
                try:
                    index_row = row.index(word[0])
                except ValueError:
                    index_row = -1
                try:
                    index_col = col.index(word[0])
                except ValueError:
                    index_col = -1

                if index_row == -1 and index_col == -1:
                    break


                if (index_row != -1) and (row[index_row:index_row + word_len] == word):
                    return True     
                
                if (index_col != -1) and (col[index_col:index_col + word_len] == word):
                    return True
                
                row = row[index_row + 1:]
                col = col[index_col + 1:]


        return False
            #for j in range(self.ROW_LENGTH - word_len + 1):
            #    if (row[j:j + word_len] == word) or (col[j:j + word_len] == word):
            #        return True
