def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def get_removal_count(nums):
    if is_sorted(nums):
        return 0

    min_sum = float("inf")
    min_sum_indx = 0
    for i in range(len(nums) - 1):
        cur_sum = nums[i] + nums[i+1]
        if cur_sum < min_sum:
            min_sum = cur_sum
            min_sum_indx = i
    
    nums[min_sum_indx]=min_sum
    nums.pop(min_sum_indx+1)
    return 1 + get_removal_count(nums)    



class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        return get_removal_count(nums)