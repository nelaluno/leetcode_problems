class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        final_sum = sum(nums)
        if final_sum % 2 != 0:
            return 0
        
        return len(nums) - 1

        