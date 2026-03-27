class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for i in range(len(mat)):
            row = mat[i]
            n = len(row)
            
            # even row -> left shift
            if i % 2 == 0:
                if row != row[k % n:] + row[:k % n]:
                    return False
            # odd row -> right shift
            else:
                if row != row[-(k % n):] + row[:-(k % n)]:
                    return False
        return True
        