from math import gcd

def check_common_str(original_str, common_srt, com_dev):
    for i in range(len(original_str)):
        if original_str[i] != common_srt[i % com_dev]:
            return False, i-1
    return True, com_dev

    

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        a, b = max(len1, len2), min(len1, len2)
        common_devisers = []

        for i in range(b, 0, -1):
            if a % i or b % i:
                continue
            common_devisers.append(i)
        
        max_com_dev = common_devisers[0]
        for com_dev in common_devisers:
            if com_dev > max_com_dev:
                continue
            
            common_str = str2[:com_dev]
            is_common, max_com_dev = check_common_str(str1, common_str, com_dev)
            if is_common:
                if com_dev < len2:
                    is_common, max_com_dev = check_common_str(str2[com_dev:], common_str, com_dev)
                    if is_common:
                        return common_str
                else:
                    return common_str
        return ""


            



        
