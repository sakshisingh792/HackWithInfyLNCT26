class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r=len(matrix)
        c=len(matrix[0])
        arr=[[0]*c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j]==-1:
                    arr[i][j]=max(matrix[k][j] for k in range(r))
                else:
                    arr[i][j]=matrix[i][j]
        return arr                
        