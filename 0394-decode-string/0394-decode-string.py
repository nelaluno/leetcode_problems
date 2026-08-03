class Solution:
    def decodeString(self, s: str) -> str:
        output = []
        numbers = []
        curr_num = 0
        curr_chs = []
        depth = 0
        for ch in s:
            if ch.isnumeric():
                curr_num = 10 * curr_num + int(ch)
                if curr_chs:
                    if depth == 0:
                        output.append("".join(curr_chs))
                    else:
                        numbers[-1][1] += "".join(curr_chs)
                    curr_chs = []
                continue
            
            if ch == "[":
                numbers.append([curr_num, ""])
                curr_num = 0
                depth += 1
                continue

            if ch == "]":
                last_num, last_str = numbers.pop()
                curr_str = (last_str + "".join(curr_chs)) * last_num
                if depth == 1:
                    output.append(curr_str)
                else:
                    numbers[-1][1] += curr_str
                curr_chs = []
                depth -= 1
                continue
            
            curr_chs.append(ch)
        
        output.extend(curr_chs)
        return "".join(output)


