class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        perfect_summ = 0
        min_abs_value = float('inf')
        negative_count = 0
        for raw in matrix:
            for value in raw:
                if value < 0:
                    negative_count += 1
                value = abs(value)
                min_abs_value = min(min_abs_value, value)
                perfect_summ += value

        # print(perfect_summ, min_abs_value)

        if negative_count % 2:
            perfect_summ -= 2 * min_abs_value
        return perfect_summ