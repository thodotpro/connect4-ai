import numpy as np

class Board:
    def __init__(self, rows: int, columns: int)->None:
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((self.rows, self.columns), dtype=int)

    def print_board(self):
        print(self.board)


if __name__ == "__main__":

    board = Board(6, 7)
    board.print_board()



