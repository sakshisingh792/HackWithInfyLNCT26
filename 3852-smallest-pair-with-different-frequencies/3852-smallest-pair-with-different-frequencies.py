class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq={}
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1

        unique=sorted(freq.keys())
        for i in range(1,len(unique)):
            if freq[unique[0]]!=freq[unique[i]]:
                return [unique[0],unique[i]]


        return [-1,-1]        


            



        