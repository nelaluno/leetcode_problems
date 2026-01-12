class Solution:
    def mark_border_region(self, i, j):
        if self.border_regions[i][j] or self.board[i][j] == "X":
            return

        self.border_regions[i][j] = 1
        if i > 0:
            self.mark_border_region(i-1, j)

        if i < self.n-1:
            self.mark_border_region(i+1, j)

        if j > 0:
            self.mark_border_region(i, j-1)

        if j < self.m-1:
            self.mark_border_region(i, j+1)
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.n = len(board)
        self.m = len(board[0])
        self.border_regions = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i in range(self.n):
            for j in [0, self.m-1]:
                if self.board[i][j] == "O" and not self.border_regions[i][j]:
                    self.mark_border_region(i, j)

        for j in range(self.m):
            for i in [0, self.n-1]:
                if self.board[i][j] == "O" and not self.border_regions[i][j]:
                    self.mark_border_region(i, j)
        
        for i in range(1, self.n-1):
            for j in range(1, self.m-1):
                if self.border_regions[i][j] or self.board[i][j] == "X":
                    continue
                self.board[i][j] = "X"

        return self.board
        

        
