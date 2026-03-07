class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        ans=[-1]*n
        for i in range(2*n-1,-1,-1):
            idx=i%n
            curel=nums[idx]
            while stack and stack[-1]<=curel:
                stack.pop()

            if i<n:
                if stack:
                    ans[i]=stack[-1]

            stack.append(curel)
        return ans                
        