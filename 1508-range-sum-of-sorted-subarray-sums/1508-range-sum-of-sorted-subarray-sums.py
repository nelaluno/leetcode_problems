MOD = 10**9 + 7


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = [0] * (n * (n + 1) // 2)
        s_i = 0
        for i in range(0, n):
            prev = 0
            for j in range(i, n):
                prev += nums[j]
                sums[s_i] = prev
                s_i += 1

        sums = sorted(sums)
        result = 0
        for i in range(left-1, right):
            result += sums[i]
            result = result % MOD

        return result

