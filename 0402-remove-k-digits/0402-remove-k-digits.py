class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack=[]
        for dig in num:
            while stack and k>0 and stack[-1]>dig:
                stack.pop()
                k-=1
            stack.append(dig) 
        while  stack and k>0:
            stack.pop() 
            k-=1
        if not stack:
            return "0"  

        res =""
        while stack:
            res+=stack[-1]
            stack.pop()
        
        res = res.rstrip('0')
        if not res:
            return "0"
        res=res[::-1]

        return res    

        