class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        visit_time = 0
        for i in range(1, len(points)):
            visit_time += max(abs(points[i-1][0] - points[i][0]), abs(points[i-1][1] - points[i][1]))
        return visit_time
