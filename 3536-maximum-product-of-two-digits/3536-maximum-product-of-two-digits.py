class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        maxm=0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                prod=int(s[i])*int(s[j])

                maxm=max(prod,maxm)
        return maxm