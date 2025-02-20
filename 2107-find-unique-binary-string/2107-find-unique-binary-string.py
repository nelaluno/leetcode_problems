class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = [int(bits, 2) for bits in nums]
        for i in range(0, 2**n):
            if i not in nums:
                str_bin = str(bin(i))[2:]
                return "0"*(n-len(str_bin)) + str_bin