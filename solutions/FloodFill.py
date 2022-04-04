class Solution:

    def validBlock(self, i: int, j: int):
        if 0 <= i < self.m and 0 <= j < self.n and self.checked[i][j] == 0 and self.image[i][j] == self.oldColor:
            return True
        else:
            return False

    def fillColor(self, i: int, j: int):
        self.image[i][j] = self.newColor
        self.checked[i][j] = 1
        if self.validBlock(i - 1, j):
            self.fillColor(i - 1, j)
        if self.validBlock(i + 1, j):
            self.fillColor(i + 1, j)
        if self.validBlock(i, j - 1):
            self.fillColor(i, j - 1)
        if self.validBlock(i, j + 1):
            self.fillColor(i, j + 1)
        return

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.newColor = newColor
        self.m = len(image)
        self.n = len(image[0])
        self.checked = [[0 for j in range(self.n)] for i in range(self.m)]
        self.oldColor = self.image[sr][sc]
        self.fillColor(sr, sc)
        return self.image



if __name__ == "__main__":
    s = Solution()
    print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2))
