from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        current_count = len([1 for ch in s[:k] if ch in vowels])
        n = len(s)
        if n == k:
            return current_count
        
        max_count = current_count
        for i in range(1, n-k+1):
            prev_is_vowel = s[i-1] in vowels
            last_is_vowel = s[i+k-1] in vowels
            current_count += last_is_vowel - prev_is_vowel
            if current_count > max_count:
                max_count = current_count
        
        return max_count