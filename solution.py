import numpy as np
import threading

class WordSearch(object):
    ROW_LENGTH = 10000
    MAX_WORD_LENGTH = 24

    def __init__(self, grid):
        arr = np.array(list(grid))
        self.grid = arr.reshape(self.ROW_LENGTH, self.ROW_LENGTH)

        self.found = False  
        self.lock = threading.Lock()

    def search_rows(self, word):
        word_len = len(word)
        for i in range(self.ROW_LENGTH):
            if self.found:
                return
            row = ''.join(self.grid[i, :])

            while True:
                try:
                    index_row = row.index(word[0])
                except ValueError:
                    index_row = -1
                    break

                if row[index_row:index_row + word_len] == word:
                    #print(self.found)
                    self.lock.acquire()
                    self.found = True
                    self.lock.release()
                    #print(self.found)
                    
                row = row[index_row + 1:]

    def search_columns(self, word):
        word_len = len(word)
        for i in range(self.ROW_LENGTH):
            if self.found:
                return
            col = ''.join(self.grid[:, i])

            while True:
                try:
                    index_col = col.index(word[0])
                except ValueError:
                    index_col = -1
                    break

                if col[index_col:index_col + word_len] == word:
                    #print(self.found)
                    self.lock.acquire()
                    self.found = True
                    self.lock.release()
                    #print(self.found)

                col = col[index_col + 1:]

    def is_present(self, word):
        self.found = False

        row_thread = threading.Thread(target=self.search_rows, args=(word,))
        col_thread = threading.Thread(target=self.search_columns, args=(word,))

        row_thread.start()
        col_thread.start()
        row_thread.join()
        col_thread.join()
        #print(col_thread.is_alive())
        #print(row_thread.is_alive())

        return self.found

    


            #for j in range(self.ROW_LENGTH - word_len + 1):
            #    if (row[j:j + word_len] == word) or (col[j:j + word_len] == word):
            #        return True
