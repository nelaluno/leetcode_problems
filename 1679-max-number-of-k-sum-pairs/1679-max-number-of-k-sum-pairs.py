from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counted_nums = defaultdict(int)
        operations = 0
        for num in nums:
            partner = k - num
            if counted_nums[partner]:
                operations += 1
                counted_nums[partner] -= 1
            else:
                counted_nums[num] += 1
        
        return operations