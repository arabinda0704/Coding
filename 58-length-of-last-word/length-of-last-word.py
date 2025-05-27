class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=len(s)
        flag=0
        kcount=0
        for i in range(n-1,-1,-1):
            if s[i]==" " and flag:
                break
            if s[i]!=" ":
                flag=1
                kcount+=1
        return kcount
        