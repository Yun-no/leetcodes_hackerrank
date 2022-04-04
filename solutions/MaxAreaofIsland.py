class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        checked = [[0 for j in range(m)] for i in range(n)]
        maxisland = 0
        def checkValid(i,j):
            if 0<=i<n and 0<=j<m and checked[i][j] == 0 and grid[i][j] == 1:
                return True
            else:
                return False
        def getIsland(i,j):
            c = 1
            checked[i][j] = 1
            if checkValid(i-1,j):
                c += getIsland(i-1,j)
            if checkValid(i+1,j):
                c += getIsland(i+1,j)
            if checkValid(i,j-1):
                c += getIsland(i,j-1)
            if checkValid(i,j+1):
                c += getIsland(i,j+1)
            return c
        for i,line in enumerate(grid):
            if sum(line)>0:
                for j in range(m):
                    if checkValid(i,j):
                        island = getIsland(i,j)
                        maxisland = max(maxisland,island)
        return maxisland


if __name__ == "__main__":
    s = Solution()
    print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))