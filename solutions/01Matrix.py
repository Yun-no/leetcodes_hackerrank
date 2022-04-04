class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i,j))
        queue = deque(queue)
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        vis = {}
        level = 0
        while len(queue) != 0:
            for _ in range(len(queue)):
                ele = queue.popleft()
                x = ele[0]
                y = ele[1]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if ele in vis:
                    continue
                vis[ele] = 1
                if mat[x][y] == 1:
                    mat[x][y] = level
                for i in range(4):
                    cx = dx[i]+ x
                    cy = dy[i]+ y
                    queue.append((cx, cy))
            level+=1
        return mat


if __name__ == "__main__":
    s = Solution()
    print(s.updateMatrix([[0,1,1,1,0,1,1,1,1,1],[0,1,1,1,1,1,0,0,1,0],[0,1,1,1,1,0,1,0,0,1],[1,1,1,0,0,1,1,1,0,1],[1,1,1,1,1,1,0,1,1,1],[0,1,1,0,1,0,0,0,0,1],[0,1,1,0,1,1,1,1,0,1],[1,1,1,1,1,0,0,1,0,1],[1,1,0,1,1,1,1,1,1,0],[1,1,1,1,1,0,0,1,0,0]]))
