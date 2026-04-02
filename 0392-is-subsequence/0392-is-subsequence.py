class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos=0
        if len(s)==0:
            return True


        for  i in range(len(t)):
            if t[i]==s[s_pos]:
                s_pos+=1
                if s_pos==len(s):
                    return True
        return False                
        
        