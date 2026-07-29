
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for i in range(len(nums)):              
            if not nums[i]:
                zero_count += 1
            else:
                nums[i-zero_count], nums[i] = nums[i], nums[i-zero_count]
            
        return nums