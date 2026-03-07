class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j=0
        k=1
        for i in range(len(nums)):
            if nums[j]!=nums[i]:
                j+=1
                nums[i],nums[j]=nums[j],nums[i]
                k+=1
        return k        

              
        