from collections import defaultdict
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        y_alligned_points = defaultdict(int)
        for x, y in points:
            y_alligned_points[y] += 1
        
        line_counts = []
        for x in y_alligned_points:
            point_count = y_alligned_points[x]
            if point_count > 1:
                line_counts.append(point_count*(point_count -1)//2)

        if len(line_counts) < 2:
            return 0

        result = 0
        module = 10**9 + 7
        summs = [0] * len(line_counts)
        prev = 0
        for ind in range(len(line_counts)-1, 0, -1):
            summs[ind-1] = prev + line_counts[ind]
            prev = summs[ind-1]

        for ind, count in enumerate(line_counts):
            result += count * summs[ind]

            if result > module:
                result = result % module

        return result