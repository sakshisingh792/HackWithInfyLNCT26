class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        flat=[]

        if m*n!=r*c:
            return mat

        for i in range(m):
            for j in range(n):
                flat.append(mat[i][j])

        index=0
        newmat=[[0]*c for _ in range(r)] 
        for i in range(r):
            for j in range(c):
                newmat[i][j]=flat[index]
                index+=1
        return newmat              

        