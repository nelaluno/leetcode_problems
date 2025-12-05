class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return len(nums)
        nums = sorted(nums)

        prev = nums[0]
        cur_sec_len = 1
        max_sec_len = 1
        for ind in range(1, len(nums)):
            if nums[ind] == prev:
                continue

            if nums[ind] - prev != 1:
                max_sec_len = max(max_sec_len, cur_sec_len)
                cur_sec_len = 0
                
            cur_sec_len += 1
            prev = nums[ind]

        max_sec_len = max(max_sec_len, cur_sec_len)
        return max_sec_len