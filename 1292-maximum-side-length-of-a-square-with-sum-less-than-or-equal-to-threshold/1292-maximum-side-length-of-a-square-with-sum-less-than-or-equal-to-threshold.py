

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:

        n, m = len(mat), len(mat[0])
        prefix_summs = [[0 for i in range(m)] for _ in range(n)]
        for i in range(n):
            raw_sum = 0
            for j in range(m):
                raw_sum += mat[i][j]
                prefix_summs[i][j] = raw_sum if i == 0 else prefix_summs[i-1][j] + raw_sum
        
        max_side = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] > threshold:
                    continue
                max_side = max(max_side, 1)
                sq_side = 2
                while i + sq_side <= n and j + sq_side <= m:
                    sq_sum = prefix_summs[i + sq_side-1][j + sq_side-1]
                    if j > 0:
                        sq_sum -= prefix_summs[i + sq_side-1][j-1]
                    if i > 0:
                        sq_sum -= prefix_summs[i-1][j + sq_side-1]
                        if j:
                            sq_sum += prefix_summs[i-1][j-1]
                    if sq_sum > threshold:
                        break
                    max_side = max(max_side, sq_side)
                    sq_side += 1

        return max_side