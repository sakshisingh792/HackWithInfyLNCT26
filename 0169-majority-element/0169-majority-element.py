class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        k=n//2
        cnt=0
        el=None
        for i in range(n):
            if cnt==0:
                cnt=1
                el=nums[i]
            elif nums[i]!=el:
                cnt-=1
            else:
                cnt+=1
        cnt1=0
        for i in range(n):
            if nums[i]==el:
                cnt+=1

        if cnt>k:
            return el  
        