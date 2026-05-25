class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq={}
        ans=[]
        for ch in nums:
            freq[ch]=freq.get(ch,0)
            if freq[ch]<k:
                ans.append(ch)
                freq[ch]+=1
        return ans        