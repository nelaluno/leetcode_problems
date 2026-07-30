class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer=[[],[]]
        set1=set(nums1)
        set2=set(nums2)
        answer[0]=list(set1-set2)
        answer[1]=list(set2-set1)
        return answer