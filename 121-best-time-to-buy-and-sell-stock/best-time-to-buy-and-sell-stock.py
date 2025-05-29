class Solution:
    def maxProfit(self,prices):
        l,r=0,1
        m_profit=0

        while r<len(prices):
            if prices[l]<prices[r]:
                m_profit=max(prices[r]-prices[l],m_profit)
            else:
                l=r
            r+=1
        return m_profit