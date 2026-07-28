class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cur_product = 1
        output = [1] * n
        for i in range(n-1):
            cur_product *= nums[i]
            output[i+1] = cur_product

        cur_product = 1
        for i in range(n-1, 0, -1):
            cur_product *= nums[i]
            output[i-1] *= cur_product

        return output

