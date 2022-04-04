class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        anc_dict = {}
        for i in range(n):
            anc_n = [l[0] for l in edges if l[1] == i]
            anc_dict[i] = anc_n
        anc_list = list(anc_dict.keys())
        anc_list.sort(key=lambda x: len(anc_dict[x]))
        anc_result = [[] for i in range(n)]
        for i in anc_list:
            anc_n = set(anc_dict[i])
            k = anc_n.copy()
            while bool(k):
                n_k = set()
                for j in k:
                    if j in anc_dict:
                        if not set(anc_dict[j]).issubset(anc_n):
                            anc_n.update(anc_dict[j])
                            n_k.update(anc_dict[j])
                k = n_k

            anc_n = list(sorted(anc_n))
            anc_dict[i] = anc_n
            anc_result[i] = anc_n
        return anc_result


if __name__ == "__main__":
    s = Solution()
    print(s.getAncestors(9,[[8,3],[6,3],[1,6],[7,0],[8,5],[2,1],[4,0],[2,3],[0,3],[5,3],[7,4],[4,1]]))
