class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bit = [int(digit) for digit in bin(start)[2:]]
        goal_bit = [int(digit) for digit in bin(goal)[2:]]
        if len(start_bit) > len(goal_bit):
            for i in range(len(start_bit) - len(goal_bit)):
                goal_bit.insert(0, 0)
        else:
            for i in range(len(goal_bit) - len(start_bit)):
                start_bit.insert(0, 0)
        return sum(i != j for i, j in zip(start_bit, goal_bit))


if __name__ == "__main__":
    s = Solution()
    print(s.minBitFlips(125,8))