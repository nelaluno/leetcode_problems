class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        merged = [""] * (2 * n)

        for i in range(n):
            merged[2 * i]  = word1[i]
            merged[2 * i + 1]  = word2[i]

        if len(word1) > n:
            merged.extend(word1[n:])
        elif len(word2) > n:
            merged.extend(word2[n:])
        
        return "".join(merged)