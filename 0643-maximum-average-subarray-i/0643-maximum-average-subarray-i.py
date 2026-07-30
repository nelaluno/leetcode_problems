class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == k:
            return sum(nums) / k
        
        
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(1, n-k+1):
            current_sum += nums[i+k-1] - nums[i-1]
            if current_sum > max_sum:
                max_sum = current_sum
        
        return max_sum / k
