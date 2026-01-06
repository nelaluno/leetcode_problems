class Solution:
    def check_sum(self, split, goal):
        # print(split, goal)
        cur_sum = 0
        for num in split:
            cur_sum += num
            if cur_sum > goal:
                return False
        
        return cur_sum == goal

    def is_magic_squere(self, grid, i_start, j_start, k):
        summ = sum(grid[i_start][j_start:j_start+k])
        # print(i_start, j_start, k, summ)
        # all rows 
        for i in range(i_start, i_start+k):
            cur_sum = 0
            if not self.check_sum(grid[i][j_start:j_start+k], summ):
                return False
        
        if not self.check_sum([grid[i_start + i][j_start + i] for i in range(k)], summ):
            return False
        
        if not self.check_sum([grid[i_start + k - i - 1][j_start + i] for i in range(k)], summ):
            return False
        
        # all colomns
        for j in range(j_start, j_start + k):
            if not self.check_sum([grid[i][j] for i in range(i_start, i_start + k)], summ):
                return False
        
        return True


    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        k = min(rows, cols)
        
        while k > 1:
            for i_start in range(rows - k + 1):
                for j_start in range(cols - k + 1):
                    if self.is_magic_squere(grid, i_start, j_start, k):
                        return k
            k -= 1
        return 1
