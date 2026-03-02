class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxstr=""
        maxlen=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                substr=s[i:j+1]
                if substr==substr[::-1]:
                    if len(substr)>maxlen:
                        maxlen=len(substr)
                        maxstr=substr
        return maxstr

        i
                
        