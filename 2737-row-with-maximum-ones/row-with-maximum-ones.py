class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi=0
        ans=[0,maxi]
        ROWS,COLS=len(mat),len(mat[0])
        for i in range(ROWS):
            cnt=0
            for j in range(COLS):
                if mat[i][j]==1:
                    cnt+=1
            if cnt>maxi:
                ans[0]=i
                ans[1]=cnt
                maxi=cnt
        return ans

        