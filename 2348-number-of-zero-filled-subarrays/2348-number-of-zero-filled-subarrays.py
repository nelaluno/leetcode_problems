class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_con_len = 0
        result = 0
        for num in nums:
            if not num:
                zero_con_len += 1
            elif zero_con_len:
                result += zero_con_len * (zero_con_len + 1) // 2
                zero_con_len = 0

        if zero_con_len:
            result += zero_con_len * (zero_con_len + 1) // 2
        return result