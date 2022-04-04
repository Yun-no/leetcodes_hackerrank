class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        init_s = s.lower()
        s_list = list(s)
        result = [init_s]
        char_list = [i for i, c in enumerate(s_list) if c.isalpha()]
        for l in range(1, len(char_list) + 1):
            for subset in itertools.combinations(char_list, l):
                new_s = init_s
                for i in subset:
                    new_s = new_s[:i] + new_s[i].upper() + new_s[i + 1:]
                result.append(new_s)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.letterCasePermutation("a1b2"))