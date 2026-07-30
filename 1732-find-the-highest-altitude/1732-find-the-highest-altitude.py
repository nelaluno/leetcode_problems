class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_sum = 0
        max_sum = 0
        for g in gain:
            cur_sum += g
            max_sum = max(max_sum, cur_sum)

        return max_sum