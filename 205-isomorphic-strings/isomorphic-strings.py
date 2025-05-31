class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s:str,t:str):
            dict={}
            if len(s)!=len(t):
                return False
            for i in range(len(s)):
                if (s[i] in dict) and (dict[s[i]]!=t[i]):
                    return False
                dict[s[i]]=t[i]
            return True        
        return helper(s,t) and helper(t,s)