class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        s_count,t_count={}, {}
        for c in s:
            if c in s_count:
                s_count[c]+=1
            else:
                s_count[c]=1
        for c in t:
            if c in t_count:
                t_count[c]+=1
            else:
                t_count[c]=1
        return s_count==t_count
        