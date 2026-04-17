class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        n=len(nums)
        diff=float("inf")
        
        for i in range(n):
            if nums[i]==target:
               
             diff=min(diff,abs(i-start))
        return diff    

        