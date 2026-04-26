class Solution:
    def validDigit(self, n: int, x: int) -> bool:
       s=str(n)
       digit=str(x)
       return digit in s and s[0] != digit