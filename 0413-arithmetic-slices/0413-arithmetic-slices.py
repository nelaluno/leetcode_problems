class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        cur_len = 1
        prev = nums.pop()
        cur_diff = None
        while nums:
            num = nums.pop()
            diff = prev - num
            # print(prev, num, diff)
            if cur_diff == diff:
                cur_len += 1
            else:
                if cur_len >= 2:
                    result += (cur_len-1)*cur_len // 2
                cur_len = 1
            # print(cur_len, result)
            prev = num
            cur_diff = diff
        
        # print(cur_len)
        if cur_len >= 2:
            result += (cur_len-1)*cur_len // 2
        
        return result
