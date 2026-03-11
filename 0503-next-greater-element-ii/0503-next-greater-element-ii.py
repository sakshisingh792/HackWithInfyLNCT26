class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i  in range(2*n-1,-1,-1):
                index=i%n
                curel=nums[index]
                while stack and stack[-1]<=curel:
                    stack.pop()
                if i<n:
                    if stack:
                        res[i]=stack[-1]
                stack.append(curel)
        return res
        