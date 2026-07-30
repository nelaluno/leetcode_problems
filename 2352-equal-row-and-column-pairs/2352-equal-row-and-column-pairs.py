from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        column_counter = defaultdict(int)
        for i in range(n):
            column_counter[tuple([grid[j][i] for j in range(n)])] += 1

        pair_count = 0
        for j in range(n):
            pair_count += column_counter[tuple(grid[j])]

        return pair_count
