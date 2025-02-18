class Solution:
    def solve(self, nums, pattern):
        curr_zero_ind = nums.index(0)
        if curr_zero_ind == 0:
            curr_num = 1
            inc = 1
        else:
            curr_num = nums[curr_zero_ind - 1]
            inc = 1 if pattern[curr_zero_ind - 1] == "I" else -1

        while curr_num > 0 and curr_num < 10:
            if curr_num in nums:
                curr_num += inc
                continue
            
            nums[curr_zero_ind] = curr_num
            if curr_zero_ind == len(nums) - 1:
                return nums
            
            nums = self.solve(nums, pattern)
            if 0 not in nums:
                return nums
            
            nums[curr_zero_ind] = 0
            curr_num += inc
        
        return nums


    def smallestNumber(self, pattern: str) -> str:
        nums = [0] * (len(pattern) + 1)
        return "".join(map(str, self.solve(nums, pattern)))
