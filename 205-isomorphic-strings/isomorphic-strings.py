class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     def helper(s:str,t:str):
    #         dict={}
    #         if len(s)!=len(t):
    #             return False
    #         for i in range(len(s)):
    #             if (s[i] in dict) and (dict[s[i]]!=t[i]):
    #                 return False
    #             dict[s[i]]=t[i]
    #         return True        
    #     return helper(s,t) and helper(t,s)

    #Alternate Approach
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True