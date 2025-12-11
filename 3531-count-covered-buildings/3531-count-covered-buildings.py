from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if len(buildings) < 5:
            return 0

        if n < 3:
            return 0
        
        x_min = defaultdict(lambda: float('inf'))
        x_max = defaultdict(int)

        y_min = defaultdict(lambda: float('inf'))
        y_max = defaultdict(int)

        for x, y in buildings:
            x_min[x] = min(x_min[x], y)
            x_max[x] = max(x_max[x], y)
            y_min[y] = min(y_min[y], x)
            y_max[y] = max(y_max[y], x)

        count = 0
        for x, y in buildings:
            if x > y_min[y] and x < y_max[y]:
                if y > x_min[x] and y < x_max[x]:
                    count += 1
        return count