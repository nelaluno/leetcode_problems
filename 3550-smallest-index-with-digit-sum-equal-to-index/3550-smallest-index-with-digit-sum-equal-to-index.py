
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            s = 0
            for ch in str(num):
                s += int(ch)
                if s > i:
                    break

            if s == i:
                return i 
                
        return -1