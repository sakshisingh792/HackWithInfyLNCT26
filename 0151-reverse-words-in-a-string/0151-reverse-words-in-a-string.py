class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
       
        i=0
        j=len(lst)-1
        while i<=j:
           
                lst[i],lst[j]=lst[j],lst[i]
                i+=1
                j-=1
            


        return " ".join(lst)    
        