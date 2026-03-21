class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxm=1
        if s=="":
            return 0
        for i in range(n):
            ans=[s[i]]
            
            

            for j in range(i+1,n):
                if s[j] not in ans:
                    ans.append(s[j])
                else:
                   
                    
                    break    
            maxm=max(maxm,len(ans))    
        return maxm