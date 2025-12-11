MOD = 10**9 + 7
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        ones_indxs = [i for i in range(len(nums)) if nums[i] == 1]
        if len(ones_indxs) < 2:
            return len(ones_indxs)

        result = 1
        last_indx = ones_indxs[0]
        for cur_indx in ones_indxs[1:]:
            result *= cur_indx - last_indx
            result = result % MOD
            last_indx = cur_indx
        return result