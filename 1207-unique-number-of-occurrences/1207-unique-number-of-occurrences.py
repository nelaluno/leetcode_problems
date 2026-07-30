from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)

        for num in arr:
            counter[num] += 1

        return len(counter) == len(set(counter.values()))