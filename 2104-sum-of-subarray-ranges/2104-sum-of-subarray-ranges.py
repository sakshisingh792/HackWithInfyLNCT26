class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for i in range(n):
            smallest=nums[i]
            largest=nums[i]
            for j in range(i,n):
                smallest=min(smallest,nums[j])
                largest=max(largest,nums[j])
                sum+=largest-smallest
        return sum        