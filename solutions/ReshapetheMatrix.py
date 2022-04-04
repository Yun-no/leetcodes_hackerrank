class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        column = row = 0
        new_mat = [[] for i in range(r)]
        if m*n == r*c:
            for i in range(m):
                while mat[i]:
                    value = mat[i].pop(0)
                    new_mat[row].append(value)
                    column += 1
                    if column == c:
                        row +=1
                        column = 0
        else:
            return mat
        return new_mat

if __name__ == "__main__":
    s = Solution()
    print(s.matrixReshape([[1,2],[3,4]],1,4))