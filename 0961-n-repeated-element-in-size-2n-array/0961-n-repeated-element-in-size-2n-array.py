from collections import defaultdict
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counts = defaultdict(int)

        for i in nums:
            counts[i] += 1
            if counts[i] == n:
                return i

