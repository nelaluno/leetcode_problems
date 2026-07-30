class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        subarray = [ch in vowels for ch in s[:k]]
        current_count = sum(subarray)
        n = len(s)
        if n == k:
            return current_count
        
        max_count = current_count
        for i in range(1, n-k+1):
            is_vowel = s[i+k-1] in vowels
            current_count += is_vowel - subarray.pop(0)
            subarray.append(is_vowel)
            if current_count > max_count:
                max_count = current_count
        
        return max_count