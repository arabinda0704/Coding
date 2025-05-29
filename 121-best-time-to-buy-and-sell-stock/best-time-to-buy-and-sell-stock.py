class Solution:
    def maxProfit(self,prices):
        l,r=0,1
        c_p=0
        m_p=0

        while r<len(prices):
            if prices[l]<prices[r]:
                m_p=max(prices[r]-prices[l],m_p)
            else:
                l=r
            r+=1
        return m_p