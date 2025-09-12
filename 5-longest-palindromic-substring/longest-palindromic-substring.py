class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) time and O(1) or O(n) space
        res=""
        maxLen=0
        # for i in range(len(s)):
        #     # for odd
        #     l,r=i,i
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if (r-l+1) > maxLen:
        #             res=s[l:r+1]
        #             maxLen=r-l+1
        #         l-=1
        #         r+=1

        #     #for even
        #     l,r=i,i+1
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if (r-l+1) > maxLen:
        #             res=s[l:r+1]
        #             maxLen=r-l+1
        #         l-=1
        #         r+=1    
        # return res

        # Practice
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>maxLen:
                    maxLen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>maxLen:
                    maxLen=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res

        # Most Optimal O(n) time and O(n) space which I also dont know how this is working-->Manacher's Algorithm
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            l, r = 0, 0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manacher(s)
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]
        