class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        max_profit = sum([prices[j]*strategy[j] for j in range(n)])
        left_sum = 0
        half_k = k // 2
        right_sum = sum([prices[j]*strategy[j] for j in range(k, n)])
        mid_sum = sum(prices[half_k:k])
        for i in range(n-k+1):
            profit = left_sum + right_sum + mid_sum
            max_profit = max(max_profit, profit)

            last = i+k
            if last != n:
                right_sum -= prices[last] * strategy[last]
                mid_sum += prices[last]

                left_sum += prices[i] * strategy[i]
                mid_sum -= prices[half_k+i]

        return max_profit