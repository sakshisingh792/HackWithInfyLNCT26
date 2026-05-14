class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        max_el=nums[0]
        if len(nums)<=max_el:
            return False

        hash_list=[0]*(max_el+1)
        for i in nums:
            hash_list[i]+=1

        for i in range(1,len(hash_list)-1):
            if hash_list[i]!=1:
                return False

        if hash_list[max_el]==2:
            return True
        else:
            return False               







        