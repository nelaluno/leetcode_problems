class Solution:
    def stringSequence(self, target: str) -> List[str]:
        a_ord = ord('a')
        prev = ""
        outs = []

        for c in target:
            if c == "a":
                outs.append(prev + "a")
            else:
                for i in range(a_ord, ord(c) + 1):
                    outs.append(prev + chr(i))
            prev = outs[-1]

        return outs
