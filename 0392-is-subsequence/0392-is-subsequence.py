class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        if len(s) > len(t):
            return False
        
        s_ind = 0
        for ch in t:
            if ch==s[s_ind]:
                s_ind += 1
                if s_ind == len(s):
                    return True

        return False
    