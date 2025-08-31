class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        m_p=0
        while r<len(prices):
            if prices[l]<prices[r]:
                m_p=max(m_p,prices[r]-prices[l])
            else:
                l=r
            r+=1
        return m_p
        