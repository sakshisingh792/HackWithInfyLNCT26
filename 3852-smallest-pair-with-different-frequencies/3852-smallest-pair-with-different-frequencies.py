class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq={}
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1

        nums.sort()
        for i in range(1,len(nums)):
            if freq[nums[0]]!=freq[nums[i]]:
                return [nums[0],nums[i]]


        return [-1,-1]        


            



        