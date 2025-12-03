from collections import defaultdict

def comb_count(n):
    # return n! / ((n-2)! * 2!)
    if n <= 1:
        return 0
    return ((n-1)* n) // 2
    


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = defaultdict(list)
        mid_to_slope = defaultdict(list)
        for ind, (x1, y1) in enumerate(points):
            for x2, y2 in points[ind+1:]:
                x_diff = (x2 - x1)
                if x_diff:
                    cur_slope = (y2 - y1) / x_diff
                else:
                    cur_slope = float('inf')
                slopes[cur_slope].append(((x1, y1), (x2, y2)))

                mid = (x1 + x2) * 10000 + (y1 + y2)
                mid_to_slope[mid].append(cur_slope)
        
        result = 0
        for slope, lines in slopes.items():
            if len(lines) < 2:
                continue

            # y = x*slope + b
            # b = y-slope*x
            b_sorted_line_counts = defaultdict(int)
            for (x1, y1), (x2, y2) in lines:
                if slope != float('inf'):
                    x_diff = (x1 - x2)
                    b = (y1 * x_diff - x1 * (y1 - y2)) / x_diff
                else:
                    b = x1
                b_sorted_line_counts[b] += 1

            if all([count == 1 for b, count in b_sorted_line_counts.items()]):
                result += comb_count(len(lines))
                continue

            prev = 0
            for b in b_sorted_line_counts:
                result += b_sorted_line_counts[b] * prev
                prev += b_sorted_line_counts[b]

        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue

            cnt = defaultdict(int)
            for k_val in mts:
                cnt[k_val] += 1

            total_sum = 0
            for count in cnt.values():
                result -= total_sum * count
                total_sum += count

        return result