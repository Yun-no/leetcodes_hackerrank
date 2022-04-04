class Solution:
    def deleteAndEarn(self, nums) -> int:
        unique_nums = collections.Counter(nums)
        prev_max, cur_max = 0, 0

        for number in range(max(unique_nums.keys()) + 1):
            prev_max, cur_max = cur_max, max(prev_max + unique_nums[number] * number, cur_max)
        return cur_max


if __name__ == "__main__":
    s = Solution()
    print(s.deleteAndEarn([2,2,3,3,3,4]))
