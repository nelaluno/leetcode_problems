
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        zero_indexes = []
        for i in range(len(nums)):
            if not nums[i]:
                zero_count += 1
                zero_indexes.append(i)
            elif zero_indexes:
                nums[zero_indexes[0]] = nums[i]
                zero_indexes.pop(0)
                zero_indexes.append(i)

        for i in range(zero_count):
            nums[-i-1] = 0
        return nums