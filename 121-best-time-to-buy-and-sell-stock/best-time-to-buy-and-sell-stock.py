class Solution:
    def maxProfit(self,prices):
        l,r=0,1
        c_p=0
        m_p=0

        while r<len(prices):
            c_p=prices[r]-prices[l]
            if prices[l]<prices[r]:
                m_p=max(c_p,m_p)
            else:
                l=r
            r+=1
        return m_p
#Internal working
sol = Solution()
# print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(Solution.maxProfit(sol,[7, 1, 5, 3, 6, 4]))