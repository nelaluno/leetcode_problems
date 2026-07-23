from itertools import combinations

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        bad_starts = set()
        for i in range(n):
            if nums[i] in bad_starts:
                continue
            i_values = set()
            i_indxs = []
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    if nums[j] not in i_values:
                        i_indxs.append(j)
                        i_values.add(nums[j])
            
            if len(i_indxs) >= 2:
                for a, b in combinations(i_indxs, 2):
                    if nums[a] < nums[b]:
                        return True
            bad_starts.add(nums[i])
        return False