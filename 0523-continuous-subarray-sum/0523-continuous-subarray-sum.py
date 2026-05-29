class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rema_freq={}
        rema_freq[0]=-1
        prefix=0
        for i in range(len(nums)):
            prefix+=nums[i]
            remainder=prefix%k
            if remainder in rema_freq:
                if i-rema_freq[remainder]>=2:
                    return True
            else:
                rema_freq[remainder]=i
                
        return False        
    
            
            




        