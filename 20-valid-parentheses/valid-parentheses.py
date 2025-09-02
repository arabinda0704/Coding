class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        for c in s:
            if c in "({[":
                d.append(c)
            else:
                if len(d)==0:
                    return False
                ch=d.pop()
                if (ch=="(" and c==")") or (ch=="{" and c=="}") or (ch=="[" and c=="]"):
                    continue
                else:
                    return False
        return len(d)==0
