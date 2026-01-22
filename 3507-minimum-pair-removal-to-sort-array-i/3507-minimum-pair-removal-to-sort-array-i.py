def get_removal_count(nums):
    print(nums)
    if all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)):
        return 0

    min_sum = float("inf")
    min_sum_indx = 0
    is_sorted = True
    for i in range(len(nums) - 1):
        cur_sum = nums[i] + nums[i+1]
        if cur_sum < min_sum:
            min_sum = cur_sum
            min_sum_indx = i

    return 1 + get_removal_count(nums[:min_sum_indx] + [min_sum] + nums[min_sum_indx+2:])    



class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        return get_removal_count(nums)