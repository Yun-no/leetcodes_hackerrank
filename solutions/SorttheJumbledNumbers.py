class Solution:

    def getindex(self, nums: int):
        r = []
        for n in str(nums):
            n = int(n)
            r.append(str(self.mapping[n]))
        return int("".join(r))

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        self.mapping = mapping
        nums.sort(key=self.getindex)
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.sortJumbled([0,1,2,3,4,5,6,7,8,9],[789,456,123]))
