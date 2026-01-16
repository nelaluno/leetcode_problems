class Solution:
    def get_diffs(self, nums, n):
        nums.insert(0, 1)
        nums.append(n)

        diffs = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                diffs.add(abs(nums[j] - nums[i]))
        return diffs

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        if n == m:
            return (n-1) ** 2
        
        h_diffs = self.get_diffs(hFences, m)
        v_diffs = self.get_diffs(vFences, n)
        

        square_sides =  h_diffs.intersection(v_diffs)
        if not square_sides or square_sides == {0}:
            return -1
    
        square_sides = max(square_sides)
        return (square_sides * square_sides) % (10**9 + 7)

        
