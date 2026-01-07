class Solution:
    def check_sum(self, split, goal, check=False):
        if not self.is_distinct(split, check=check):
            return False
        
        cur_sum = 0
        for num in split:
            cur_sum += num
            if cur_sum > goal:
                return False
        
        return cur_sum == goal

    def is_distinct(self, nums, check=False):
        nums = set(nums)
        if len(nums) == 1:
            return False

        if check:        
            for num in nums: 
                if num < 1 or num > 9:
                    return False
                    
        return True 

    def is_magic_squere(self, grid, i_start, j_start, k):
        if not self.is_distinct(grid[i_start][j_start:j_start+k], check=True) or 0 in grid[i_start][j_start:j_start+k]:
            return False

        summ = sum(grid[i_start][j_start:j_start+k])
        # all rows 
        for i in range(i_start+1, i_start+k):
            cur_sum = 0
            if not self.check_sum(grid[i][j_start:j_start+k], summ, check=True):
                return False
        
        if not self.check_sum([grid[i_start + i][j_start + i] for i in range(k)], summ):
            return False
        
        if not self.check_sum([grid[i_start + k - i - 1][j_start + i] for i in range(k)], summ):
            return False
        
        # all columns
        for j in range(j_start, j_start + k):
            if not self.check_sum([grid[i][j] for i in range(i_start, i_start + k)], summ):
                return False
        
        return True


    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        k = 3
        if rows < k or cols < k:
            return 0
        
        count = 0
        for i_start in range(rows - k + 1):
            for j_start in range(cols - k + 1):
                if self.is_magic_squere(grid, i_start, j_start, k):
                    count += 1
        return count