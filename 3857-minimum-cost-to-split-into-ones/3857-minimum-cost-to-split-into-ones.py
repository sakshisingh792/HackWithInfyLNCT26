class Solution:
    def minCost(self, n: int) -> int:
        cost=0
        while n>0:
            n=1*n-1
            cost+=n
        return cost    
        