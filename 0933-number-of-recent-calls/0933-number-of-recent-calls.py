class RecentCounter:
    def __init__(self):
        self.calls = []
        self.start_ind = 0

    def ping(self, t: int) -> int:
        prev_calls_count = 0
        if self.calls:
            new_start_found = False
            for i in range(self.start_ind, len(self.calls)):
                if t - self.calls[i] <= 3000:
                    self.start_ind = i
                    new_start_found = True
                    break
            if new_start_found:
                prev_calls_count = len(self.calls) - self.start_ind
            else:
                prev_calls_count = 0
                self.start_ind = len(self.calls)

        self.calls.append(t)
        return prev_calls_count + 1



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)