class Solution:
    def summ(self,a:List[int])->int:
        sum=0
        for i in range(len(a)):
            sum+=a[i]
        return sum
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # O(k) TC
        n=len(cardPoints)
        l=0
        r=n-k
        total=self.summ(cardPoints[r:])#We can simply use inbuild sum function
        res=total
        while r<n:
            total+=cardPoints[l]-cardPoints[r]#Adding lth index element and subtracting rth inex element
            res=max(res,total)
            l+=1
            r+=1
        return res
            
