MOD = 10**9 + 7

class Solution:
    def get_diffs(self, nums, n):
        nums = [1] + sorted(nums) + [n]

        diffs = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                diffs.add(nums[j] - nums[i])
        return diffs

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        if n == m:
            return (n-1) ** 2
        
        h_diffs = self.get_diffs(hFences, m)

        vFences = [1] + sorted(vFences) + [n]
        max_sq_side = 0
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                value = vFences[j] - vFences[i]
                if value in h_diffs:
                    max_sq_side = max(value, max_sq_side)

        if not max_sq_side:
            return -1
    
        return (max_sq_side * max_sq_side) % MOD

        
