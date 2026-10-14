class MinimaxGaming:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.ai = 'X'
        self.opponent = 'O'

    def print_board(self):
        for row in self.board:
            print("|" + "|".join(row) + "|")
        print()

    def is_moves_left(self):
        return any(cell == ' ' for row in self.board for cell in row)

    def evaluate(self):
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return 10 if row[0] == self.ai else -10

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return 10 if self.board[0][col] == self.ai else -10

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return 10 if self.board[0][0] == self.ai else -10

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return 10 if self.board[0][2] == self.ai else -10

        return 0

    def minimax(self, depth, is_max):
        score = self.evaluate()

        if score == 10 or score == -10:
            return score
        if not self.is_moves_left():
            return 0

        if is_max:
            best = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.ai
                        best = max(best, self.minimax(depth + 1, False))
                        self.board[i][j] = ' '
            return best
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.opponent
                        best = min(best, self.minimax(depth + 1, True))
                        self.board[i][j] = ' '
            return best

    def find_best_move(self):
        best_val = -float('inf')
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.ai
                    move_val = self.minimax(0, False)
                    self.board[i][j] = ' '

                    if move_val > best_val:
                        best_val = move_val
                        best_move = (i, j)
        return best_move

game = MinimaxGaming()
game.board = [
    ['X', 'O', 'X'],
    ['O', 'O', ' '],
    [' ', ' ', 'X']
]

print("Initial Game Board State:")
game.print_board()

best_row, best_col = game.find_best_move()
print(f"Optimal AI Move selected by Minimax: Row {best_row}, Column {best_col}")
