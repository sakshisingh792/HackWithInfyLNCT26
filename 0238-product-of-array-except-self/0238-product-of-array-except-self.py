class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m=len(nums)
        left=1
        ans=[1]*m
        for i in range(m):
            ans[i]*=left
            left*=nums[i]
        right=1
        for i in range(m-1,-1,-1):
            ans[i]*=right
            right*=nums[i]
        return ans        

        