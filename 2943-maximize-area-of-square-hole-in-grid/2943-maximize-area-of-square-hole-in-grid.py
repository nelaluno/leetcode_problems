
class Solution:
    def get_max_seq_len(self, n, seq):
        seq = sorted(seq)
        last_value = None
        count = 0
        max_count = 0
        for value in seq:
            if value > 1 and value < n:
                if not last_value or value - last_value == 1:
                    count += 1
                else:
                    max_count = max(count, max_count)
                    count = 1
                last_value = value
        max_count = max(count, max_count)
        return max_count + 1
    
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        n += 2
        m += 2

        hb = self.get_max_seq_len(n, hBars)
        vb = self.get_max_seq_len(m, vBars)
        squere_side = min(hb, vb)
        return squere_side * squere_side


        

            