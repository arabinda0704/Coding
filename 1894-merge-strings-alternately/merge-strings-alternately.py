class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=len(word1)
        n=len(word2)
        res=""
        for i in range(max(m,n)):
            if i<m:
                res+=word1[i]
            if i <n:
                res+=word2[i]

        return res