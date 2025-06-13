class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        #Brute Force
        # count=0
        # for i in range(len(s)):
        #     seen={"a":0,"b":0,"c":0}
        #     for j in range(i,len(s)):
        #         if s[j] in seen:
        #             seen[s[j]]+=1
        #         if seen['a'] > 0 and seen['b'] > 0 and seen['c'] > 0:
        #             count+=1
        # return count

        #Better
        # count = 0
        # for i in range(len(s)):
        #     seen = {'a': 0, 'b': 0, 'c': 0}
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             seen[s[j]] += 1
        #         if seen['a'] > 0 and seen['b'] > 0 and seen['c'] > 0:
        #             count += (len(s) - j)
        #             break
        # return count

        #Both the above code give TLE
        #optimal
        lastSeen={"a":-1,"b":-1,"c":-1}
        res=0
        for i in range(len(s)):
            lastSeen[s[i]]=i
            if lastSeen["a"] !=-1 and lastSeen["b"] !=-1 and lastSeen["c"] !=-1:
                res+=(1+min(lastSeen["a"],lastSeen["b"],lastSeen["c"]))
        return res


        