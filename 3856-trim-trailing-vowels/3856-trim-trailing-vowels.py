class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowel="aeiou"
        i=len(s)-1
        while i>=0 and s[i] in vowel:
            i-=1
        

        lst=[]
        for j in range(i+1):
            lst.append(s[j])

        return "".join(lst)    
         
            
        