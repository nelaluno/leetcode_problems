class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        visit_time = 0
        prev_point = points[0]
        for point in points[1:]:
            visit_time += max(abs(prev_point[0] - point[0]), abs(prev_point[1] - point[1]))
            prev_point = point
        return visit_time
