class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        m=len(v1)
        n=len(v2)
        i=0
        while i<m or i <n:
            a=int(v1[i]) if i<m else 0
            b=int(v2[i]) if i<n else 0
            if a<b:
                return -1
            elif a>b:
                return 1
            i+=1
        return 0  

