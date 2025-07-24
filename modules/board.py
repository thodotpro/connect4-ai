import numpy as np

class Board:
    def __init__(self, rows: int, columns: int)->None:
        self.rows = rows
        self.columns = columns
        self._board = np.zeros((self.rows, self.columns), dtype=int)

    def drop_piece(self, col: int)->None:
        pass

    def _is_valid_drop(self, col: int)->bool:
        pass

    def check_win(self)->bool:
        pass

    def _check_horizontal_win(self)->bool:
        pass

    def _check_vertical_win(self)->bool:
        pass

    def _check_diagonal_left_win(self)->bool:
        pass

    def _check_diagonal_right_win(self)->bool:
        pass


    def print_board(self)->None:
        print(self._board)


if __name__ == "__main__":

    board = Board(6, 7)
    board.print_board()


