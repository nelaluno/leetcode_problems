class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        output = len(prices)
        cur_len = 1
        prev = prices[0]
        for ind, p in enumerate(prices[1::]):
            if prev - p == 1:
                cur_len += 1
            else:
                output += (cur_len) * (cur_len - 1) // 2
                cur_len = 1
            # print(prev, p, cur_len, output)
            prev = p

        if cur_len > 1:
            output += (cur_len) * (cur_len - 1) // 2
            
        return output