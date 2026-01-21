class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            
            candidate = -1
            bin_num = bin(num)[2:]
            for i in range(len(bin_num)-1,-1, -1):
                if bin_num[i] == "0":
                    break
            if i < len(bin_num)-1:
                if i == 0:
                    candidate = int(f"0b{bin_num[1:]}", 2)
                else:
                    candidate = int(f"0b{bin_num[:i+1]}0{bin_num[i+2:]}", 2)
            result.append(candidate)
        return result