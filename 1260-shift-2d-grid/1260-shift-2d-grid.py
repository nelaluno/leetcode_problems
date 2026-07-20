from collections import deque

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        num = n * m
        k = k % num

        if k == 0:
            return grid
        
        vector = deque([0] * num)
        for i in range(n):
            for j in range(m):
                vector[m*i + j] = grid[i][j]

        vector.rotate(k)

        for i in range(n):
            for j in range(m):
                grid[i][j] = vector[m*i + j]

        return grid


        