class Solution:
    def stringSequence(self, target: str) -> List[str]:
        outs = ["a"]
        curr_srt = ["a"]
        curr_ind = 0
        n = len(target)
        while len(curr_srt) != n or curr_srt[-1] != target[-1]:
            # print(curr_srt, outs)
            if curr_srt[curr_ind] == target[curr_ind]:
                curr_srt.append("a")
                outs.append("".join(curr_srt))
                curr_ind += 1
                continue
            
            curr_srt[curr_ind] = chr(ord(curr_srt[curr_ind]) + 1)
            outs.append("".join(curr_srt))
        return outs
