class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cur_product = 1
        prefix_products = [0] * n
        for i in range(n-1):
            cur_product *= nums[i]
            prefix_products[i+1] = cur_product

        cur_product = 1
        suffix_products = [0] * n
        for i in range(n-1, 0, -1):
            cur_product *= nums[i]
            suffix_products[i-1] = cur_product

        output = [0] * n
        output[0] = suffix_products[0]
        output[n-1] = prefix_products[n-1]
        for i in range(1, n-1):
            output[i] = prefix_products[i] * suffix_products[i]

        return output

