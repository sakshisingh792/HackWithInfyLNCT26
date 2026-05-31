class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def parenthesis(openn,close,output):
            if openn==0 and close==0:
                ans.append(output)
                return 

            if openn!=0:
                parenthesis(openn-1,close,output+"(")

            if openn<close:
                parenthesis(openn,close-1,output+")")

        parenthesis(n,n,"")
        return ans                