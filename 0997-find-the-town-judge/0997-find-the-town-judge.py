from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1 if n > 1 else 1

        trusters, trustees = [0]*n, [0]*n

        for a, b in trust:
            trusters[a-1] += 1
            trustees[b-1] += 1

        for j in range(n):
            if trusters[j] == 0 and trustees[j] == n-1:
                return j+1
        
        return -1