class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        first_ind = 0
        last_ind = 0
        zero_count = int(nums[0] == 0)
        max_len = 0
        while last_ind < len(nums):
            if zero_count <= k:
                max_len = max(max_len, (last_ind-first_ind+1))  
                last_ind += 1
                if  last_ind == len(nums):
                    break
                zero_count += nums[last_ind] == 0                
            else:
                if first_ind == last_ind:
                    last_ind += 1
                    if last_ind == len(nums):
                        break
                    zero_count = nums[last_ind] == 0
                else:
                    zero_count -= nums[first_ind] == 0
                first_ind += 1
                
        return max_len