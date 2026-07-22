from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return -1 if n > 1 else 1
        
        trust_lists = defaultdict(list) 
        potential_judges = set(range(1, n+1))

        for a, b in trust:
            if a in potential_judges:
                potential_judges.remove(a)
            trust_lists[a].append(b)

        if len(trust_lists) != n-1:
            return -1

        for j in potential_judges:
            is_judge = True
            for a, t_list in trust_lists.items():
                if j not in t_list:
                    is_judge = False
                    break
            if is_judge:
                return j
                    
        return -1