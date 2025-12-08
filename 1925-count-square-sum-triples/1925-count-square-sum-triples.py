class Solution:
    def countTriples(self, n: int) -> int:
        squares = [n**2 for n in range(1, n+1)]
        squares_set = set(squares)
        count = 0
        for ind_a in range(n):
            for ind_b in range(ind_a+1, n):
                sq_sum = squares[ind_a] + squares[ind_b]
                if sq_sum > squares[-1]:
                    break
                if sq_sum in squares_set:
                    count += 2
        return count