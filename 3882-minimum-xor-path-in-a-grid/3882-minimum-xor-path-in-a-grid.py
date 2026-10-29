class Solution:

    
    def minCost(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        costs = [[list() for _ in range(m)] for __ in range(n)]
        costs[0][0] = [grid[0][0]]

        for i in range(n):
            for j in range(m):
                if i > 0:
                    costs[i][j].extend([cost ^ grid[i][j] for cost in costs[i-1][j]])

                if j > 0:
                    costs[i][j].extend([cost ^ grid[i][j] for cost in costs[i][j-1]])
            
                costs[i][j] = list(set(costs[i][j]))

        return min(costs[i][j])
            