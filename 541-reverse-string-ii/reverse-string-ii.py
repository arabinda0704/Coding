class Solution:
    def reverse(self,s):
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return ''.join(s)
    def reverseStr(self, s: str, k: int) -> str:
        # n=len(s)
        # res=""
        # if n<k:
        #     return self.reverse(s)
        # l,r=0,k
        # while l<n:
        #     res+= self.reverse(s[l:r])
        #     res+=s[r:r+k]
        #     l += 2 * k
        #     r = l + k
        # return res
        
        #Better
        s=list(s)
        for i in range(0,len(s),2*k):
            s[i:i+k]=self.reverse(s[i:i+k])
        return "".join(s)


        