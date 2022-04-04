class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target:
            return 0
        else:
            if target >= (startValue - 1) * 2:
                if target % 2 == 0:
                    return self.brokenCalc(startValue, (target + 1) // 2) + 1
                else:
                    return self.brokenCalc(startValue, (target + 1) // 2) + 2
            elif startValue < target < (startValue - 1) * 2:
                if target % 2 == 0:
                    return startValue - (target + 1) // 2 + 1
                else:
                    return startValue - (target + 1) // 2 + 2

            elif target < startValue:
                return startValue - target



if __name__ == "__main__":
    s = Solution()
    print(s.brokenCalc(4,12))