class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ROWS,COLS=len(accounts),len(accounts[0])
        maxi=accounts[0][0]
        for i in range(ROWS):
            summ=0
            for j in range(COLS):
                summ+=accounts[i][j]
            maxi=max(summ,maxi)
        return maxi

        