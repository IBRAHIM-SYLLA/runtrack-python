class Board:
    def __init__(self, size):
        self.size = [size * ['O']] * size

    def board(self):
        for ligne in self.size:
            print(' '.join(ligne))

    def play()
board = Board(6)
board.board()
print(board)