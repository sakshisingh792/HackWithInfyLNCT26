class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n=len(rungs)
        ans=0
        if rungs[0]>dist:
            ans+=(rungs[0]-1)//dist
         

        for i in range(n-1):
            diff=rungs[i+1]-rungs[i]
            if diff>dist:
                ans+=(diff-1)//dist
        return ans        


        