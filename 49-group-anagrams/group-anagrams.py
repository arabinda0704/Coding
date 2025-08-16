class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     res[tuple(count)].append(s)
        # return list(res.values())
        #Another
        # res = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))  # sorting gives a canonical form
        #     res[key].append(s)
        # return list(res.values())

        #Another
        res = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in res:
                res[key]=[]
            res[key].append(s)
        return list(res.values())