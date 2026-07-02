class Solution:

    def check_col(self, i:int, j:int) -> bool:
        for k in range(0,self.length):
            if k!=i and self.board[i][j] != '.' and self.board[k][j] == self.board[i][j]:
                return False
        return True

    def check_row(self, i:int, j:int) -> bool:
        for k in range(0, self.length):
            if k!=j and self.board[i][j] != '.' and self.board[i][k] == self.board[i][j]:
                return False
        return True

    def check_grid(self, i:int, j:int) -> bool:
        x_i = i - i%3
        y_i = j - j%3
        for k in range(0,3):
            for l in range(0,3):
                if (x_i + k) != i and (y_i + l) != j and self.board[i][j] != '.' and self.board[x_i + k][y_i + l] == self.board[i][j]:
                    return False
        return True
                

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.length = len(board)
        self.board = board

        for i in range(0,self.length):
            for j in range(0,self.length):
                if not (self.check_row(i,j) and self.check_col(i,j) and self.check_grid(i,j)):
                    return False
        return True

        