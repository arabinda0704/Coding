class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i,j=0,0
        res=[]
        while i<len(s) and j <len(spaces):
            if i <spaces[j]:
                res.append(s[i])
                i+=1
            else:
                res.append(" ")
                j+=1
        res+=s[i:]

        return "".join(res)
        