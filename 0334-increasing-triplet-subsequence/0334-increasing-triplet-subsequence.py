class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = sys.maxsize 
        second_min = sys.maxsize 
        for n in nums:
            if n <= first_min:
                first_min = n
            elif n <= second_min:
                second_min = n
            else:
                return True

        return False