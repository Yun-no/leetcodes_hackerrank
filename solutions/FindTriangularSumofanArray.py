class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
        	nums = [(nums[i] + nums[i+1]) % 10 for i in range(len(nums)-1)]
        return nums[0]


if __name__ == "__main__":
    s = Solution()
    print(s.triangularSum([1,2,3,4,5,7,9]))