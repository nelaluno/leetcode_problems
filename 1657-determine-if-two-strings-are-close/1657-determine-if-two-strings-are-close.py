from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False

        counter1 = defaultdict(int)
        for ch in word1:
            counter1[ch] += 1

        counter2 = defaultdict(int)
        for ch in word2:
            counter2[ch] += 1
        
        return sorted(list(counter1.values())) == sorted(list(counter2.values()))