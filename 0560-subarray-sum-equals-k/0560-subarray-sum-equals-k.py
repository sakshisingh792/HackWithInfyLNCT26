class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_pre={}
        freq_pre[0]=1
        prefix=0
        ans=0
        
        for i in range(len(nums)):
            prefix+=nums[i]
            if (prefix-k ) in freq_pre:
                ans+=freq_pre[prefix-k]
             
            if prefix in freq_pre:
                freq_pre[prefix]+=1
            else:
                freq_pre[prefix]=1
        return ans            

