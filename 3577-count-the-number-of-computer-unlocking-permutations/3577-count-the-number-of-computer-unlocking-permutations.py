class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7

        decrypted_compl = complexity[0]
        for compl in complexity[1:]:
            if compl <= decrypted_compl:
                return 0

        factorial = 1
        for i in range(1, len(complexity)):
            factorial *= i
            factorial = factorial % mod
        return factorial