class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr=[]
        left=[]
        right=[]
        mid=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                left.append(nums[i])
            elif nums[i]>pivot:
                right.append(nums[i])
            else:
                mid.append(nums[i])    

        return left+mid+right      

        