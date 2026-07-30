class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        is_vowel = [ch in vowels for ch in s]
        
        current_count = sum(is_vowel[:k])
        n = len(s)
        if n == k:
            return current_count
        
        max_count = current_count
        for i in range(1, n-k+1):
            current_count += is_vowel[i+k-1] - is_vowel[i-1]
            if current_count > max_count:
                max_count = current_count
        
        return max_count