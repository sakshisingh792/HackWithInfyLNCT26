class Solution:

    def largest_rec(self,arr,n):
        next_smal=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while  stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if  not stack :
                next_smal[i]=n
            else:
                next_smal[i]=stack[-1]
            stack.append(i)


        prev_smal=[0]*n
        stack=[] 
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if not stack:
                prev_smal[i]=-1
            else:
                prev_smal[i]=stack[-1]
            stack.append(i)    


        area=0
        max_area=float("-inf")
        for i in range(n):
            l=arr[i]
            b=next_smal[i]-prev_smal[i]-1
            area=l*b
            max_area=max(area,max_area)
        return max_area                    

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0]*n

        max_area = 0

        for i in range(len(matrix)):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            max_area = max(max_area, self.largest_rec(heights, n))

        return max_area                
        