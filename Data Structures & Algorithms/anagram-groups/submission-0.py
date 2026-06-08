class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            s_sorted = sorted(s)
            print(s_sorted)
            s_join = ''.join(s_sorted)
            res[s_join].append(s)
        return list(res.values())
        