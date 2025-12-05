
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        
        medium = num // 3
        return [medium-1, medium, medium+1]