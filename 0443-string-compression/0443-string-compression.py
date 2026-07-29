class Solution:
    def compress(self, chars: List[str]) -> int:
        compressed_string = []
        group_count = 0
        for ch in chars:
            if compressed_string and compressed_string[-1] == ch:
                group_count += 1
            else:
                if compressed_string:
                    if group_count > 1:
                        compressed_string.append(group_count)
                compressed_string.append(ch)
                group_count = 1

        if group_count > 1:
            compressed_string.append(group_count)
        
        chars.clear()
        chars += list("".join([str(s) for s in compressed_string]))
        return len(chars)