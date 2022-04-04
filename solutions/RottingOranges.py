class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        new_rotten = []
        fresh = []
        empty = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    new_rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh.append((i,j))
                else:
                    empty.append((i,j))
        if len(fresh) == 0:
            return 0
        new_rotten = deque(new_rotten)
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        checked = {}
        step = 0
        while len(fresh)>0 and len(new_rotten)>0:
            for _ in range(len(new_rotten)):
                rotten = new_rotten.popleft()
                x = rotten[0]
                y = rotten[1]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if rotten in checked or rotten in empty:
                    continue
                if rotten in fresh:
                    fresh.remove(rotten)
                checked[rotten] = 1
                for i in range(4):
                    cx = dx[i]+ x
                    cy = dy[i]+ y
                    new_rotten.append((cx, cy))
            step += 1
        if len(fresh)>0:
            return -1
        else:
            return step - 1


if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
