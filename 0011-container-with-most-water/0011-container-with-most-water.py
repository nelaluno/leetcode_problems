class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ind = 0
        right_ind = len(height) - 1
        max_squere = 0

        while left_ind < right_ind:
            squere = (right_ind - left_ind) * min(height[left_ind], height[right_ind])
            max_squere = max(max_squere, squere)
            if height[left_ind] >= height[right_ind]:
                right_ind -= 1
            elif height[left_ind] < height[right_ind]:
                left_ind += 1
        
        return max_squere