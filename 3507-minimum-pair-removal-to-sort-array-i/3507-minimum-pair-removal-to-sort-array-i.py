def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        op_count = 0
        while not is_sorted(nums):
            min_sum = float("inf")
            min_sum_indx = 0
            for i in range(len(nums) - 1):
                cur_sum = nums[i] + nums[i+1]
                if cur_sum < min_sum:
                    min_sum = cur_sum
                    min_sum_indx = i
                
            nums[min_sum_indx]=min_sum
            nums.pop(min_sum_indx+1)
            op_count += 1
        return op_count
