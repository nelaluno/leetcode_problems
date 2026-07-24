class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        merged = [""] * (len(word1) + len(word2))

        for i in range(n):
            merged[2 * i]  = word1[i]
            merged[2 * i + 1]  = word2[i]
        
        print(merged)
        if len(word1) > n:
            merged[2*n:] = word1[n:]
        elif len(word2) > n:
            merged[2*n:] = word2[n:]
        
        return "".join(merged)