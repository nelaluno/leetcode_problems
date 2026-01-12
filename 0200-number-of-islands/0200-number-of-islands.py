class Solution:
    def sinkIsland(self, i, j):
        self.grid[i][j] = "0"
        if i > 0 and self.grid[i-1][j] == "1":
            self.sinkIsland(i-1, j)
        if i < self.n - 1 and self.grid[i+1][j] == "1":
            self.sinkIsland(i+1, j)
        if j > 0 and self.grid[i][j-1] == "1":
            self.sinkIsland(i, j-1)
        if j < self.m - 1 and self.grid[i][j+1] == "1":
            self.sinkIsland(i, j+1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n = len(self.grid)
        self.m = len(self.grid[0])
        num = 0
        
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == "0":
                    continue
                
                num += 1
                self.sinkIsland(i, j)

        return num
                