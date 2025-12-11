from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if len(buildings) < 5:
            return 0

        if n < 3:
            return 0

        x_sorted = defaultdict(list)
        y_min = defaultdict(lambda: float('inf'))
        y_max = defaultdict(int)


        for x, y in buildings:
            x_sorted[x].append(y)
            y_min[y] = min(y_min[y], x)
            y_max[y] = max(y_max[y], x)

        count = 0
        for x in x_sorted:
            if len(x_sorted) < 3:
                continue
            x_sorted[x] = sorted(x_sorted[x])

            # first and last y are not covered
            for i in range(1, len(x_sorted[x])- 1):
                
                y = x_sorted[x][i]
                if x > y_min[y] and x < y_max[y]:
                    count += 1
        return count