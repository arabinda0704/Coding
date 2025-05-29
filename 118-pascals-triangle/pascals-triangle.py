class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def generateRow(row: int)->List[int]:
            ans=1
            ansRow=[]
            ansRow.append(1)
            for i in range(1,row):
                ans*=(row-i)
                ans//=i
                ansRow.append(ans,)
            return ansRow
        f_ans=[]
        for i in range(1,numRows+1):
            f_ans.append(generateRow(i))
        return f_ans


        