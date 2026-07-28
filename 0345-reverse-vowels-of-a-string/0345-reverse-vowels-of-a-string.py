VOWELS = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}


class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        s_list = list(s)
        
        start_ind, end_ind = 0, len(s) - 1
        is_start_vowel, is_end_vowel = s_list[start_ind] in VOWELS, s_list[end_ind] in VOWELS
        while end_ind > start_ind:
            if is_start_vowel:
                if is_end_vowel:
                    s_list[start_ind], s_list[end_ind] = s_list[end_ind], s_list[start_ind]
                    start_ind += 1
                    end_ind -= 1
                    is_start_vowel, is_end_vowel = s_list[start_ind] in VOWELS, s_list[end_ind] in VOWELS
                else:
                    end_ind -= 1
                    is_end_vowel = s_list[end_ind] in VOWELS
            else:
                if is_end_vowel:
                    start_ind += 1
                    is_start_vowel = s_list[start_ind] in VOWELS
                else:
                    start_ind += 1
                    end_ind -= 1
                    is_start_vowel, is_end_vowel = s_list[start_ind] in VOWELS, s_list[end_ind] in VOWELS

        return "".join(s_list)
