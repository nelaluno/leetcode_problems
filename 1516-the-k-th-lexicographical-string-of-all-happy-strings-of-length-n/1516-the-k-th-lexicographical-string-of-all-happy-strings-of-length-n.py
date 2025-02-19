class Solution:
    def is_happy(self, s):
        last = s[0]
        for i in range(1, len(s)):
            if s[i] == last:
                return False
            last = s[i]
        return True

    def get_next(self, s):
        while True:
            if s == self.stopper:
                return None

            goal_ind = max([i for i in range(len(s)) if s[i] != 3])
            set_one = True
            if s[goal_ind] < 3:
                s[goal_ind] += 1
                if goal_ind + 1 < len(s):
                    for i in range(goal_ind + 1, len(s)):
                        s[i] = 1 if set_one else 2
                        set_one = not set_one

            if self.is_happy(s):
                return s

    def solve(self, n, k):
        self.stopper = [3 if not (i % 2) else 2 for i in range(n)]
        happy_nums = [1, 2, 3]
        happy_str_ind = 1
        happy_str = [1 if not (i % 2) else 2 for i in range(n)]
        if k == 1:
            return happy_str
        last_letter = happy_str[-1]

        while happy_str_ind != k:
            happy_str = self.get_next(happy_str)
            happy_str_ind += 1
            
            if not happy_str:
                break

        return happy_str

    def getHappyString(self, n: int, k: int) -> str:
        if k > 3**n:
            return ""
        happy_letters = {1: 'a', 2:'b', 3:'c'}
        happy_nums = self.solve(n, k)
        if not happy_nums:
            return ""
        else:
            return "".join([happy_letters[n] for n in happy_nums])
