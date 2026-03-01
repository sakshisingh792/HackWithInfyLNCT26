class Solution:
    def numSteps(self, s: str) -> int:
        n=int(s,2)
        step=0
        while n!=1:
            if n%2==0:
                n=n//2
                step+=1
            elif n%2==1:
                n=n+1 
                step+=1   
        return step
        