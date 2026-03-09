class Solution:
    def minOperations(self, s: str) -> int:
        start_0=0
        start_1=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]!="0":
                    start_0+=1
                if s[i]!="1":
                    start_1+=1
            else:
                if s[i]!="1":
                    start_0+=1
                if s[i]!="0":
                    start_1+=1
        return min(start_0,start_1)                        


                
        

        