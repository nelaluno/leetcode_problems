
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counts = {}

        for i in nums:
            if i in counts:
                return i
            counts[i] = 1

