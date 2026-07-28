class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        s_vowels = []
        for i in range(len(s)):
            if s_list[i].lower() in vowels:
                s_vowels.append(s_list[i])

        v_ind = 0
        for i in range(len(s)):
            if s_list[i].lower() in vowels:
                s_list[i] = s_vowels[-v_ind-1]
                v_ind += 1

        return "".join(s_list)
