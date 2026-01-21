class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            candidate = -1
            if num % 2:
                for j in range(num):
                    if (j | (j + 1)) == num:
                        candidate = j
                        break
            result.append(candidate)
        return result