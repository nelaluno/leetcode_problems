class Solution:
    def countTriples(self, n: int) -> int:
        squares = [n**2 for n in range(1, n+1)]
        squares_set = set(squares)
        # print("squares", squares)
        count = 0
        for ind_a in range(n):
            for ind_b in range(ind_a+1, n):
                # print("check", squares[ind_a], squares[ind_b])
                sq_sum = squares[ind_a] + squares[ind_b]
                if sq_sum > squares[-1]:
                    # print(sq_sum, ">", squares[-1])
                    break
                if sq_sum in squares_set:
                    # (a, b) and (b, a)
                    count += 2
                    # print(ind_a, ind_b)
        return count