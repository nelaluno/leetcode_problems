class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        visit_time = 0
        prev_point = points[0]
        for point in points[1:]:
            x_move = abs(prev_point[0] - point[0])
            y_move = abs(prev_point[1] - point[1])
            visit_time += max(x_move, y_move)
            # if y_move == 0:
            #     visit_time += x_move
            # elif x_move == 0:
            #     visit_time += y_move
            # else:
            #     visit_time += max(x_move, y_move)
            #     if x_move >= y_move:
            #         visit_time += x_move
            #     else:
            #         visit_time += y_move
            # print(point, visit_time)
            prev_point = point
        return visit_time
