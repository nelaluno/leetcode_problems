class Solution:
    def removeStars(self, s: str) -> str:
        fragments = []
        fr_start = 0
        star_count = 0
        for i in range(len(s)):
            if s[i] == '*':
                star_count += 1
                if i != len(s) - 1:
                    continue
            
            if star_count:
                fr_end = i-star_count*2 + (s[i] == '*')
                if fr_start < fr_end:
                    fragments.append(s[fr_start:fr_end])
                elif fr_end < fr_start and fragments:
                    remove_len = fr_start - fr_end
                    while remove_len > 0:
                        last_fr_len = len(fragments[-1])
                        if last_fr_len > remove_len:
                            fragments[-1] = fragments[-1][:-remove_len]
                        else:
                            fragments.pop()
                        remove_len -= last_fr_len
                fr_start = i
                star_count = 0
                
        if star_count == 0 and s[i] != '*':
            fragments.append(s[fr_start:])

        return "".join(fragments)