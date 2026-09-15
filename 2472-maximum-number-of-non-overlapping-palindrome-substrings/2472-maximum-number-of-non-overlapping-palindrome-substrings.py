
from collections import defaultdict

def is_palindrome(s, i_start, i_end):
    for i in range((i_end - i_start + 1) // 2):
        if s[i_start + i] != s[i_end - i]:
            return False
    return True


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        min_double_count = k // 2

        palindrome_count = 0
        ch_inds = defaultdict(list)
        double_count = 0
        for i, ch in enumerate(s):
            ch_inds[ch].append(i)
            double_count += (len(ch_inds[ch]) % 2 == 0)
            if len(ch_inds[ch]) > 1 and double_count >= min_double_count:
                for i_start in ch_inds[ch][:-1]:
                    if (i - i_start + 1) < k:
                        break

                    if is_palindrome(s, i_start, i):
                        palindrome_count += 1
                        double_count = 0
                        ch_inds = defaultdict(list)
                        break
        return palindrome_count
