class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        if len(score)==1:
            return score
        m=len(score)
        n=len(score[0])
        for i in range(m):
            maxx=i
            #Selection sort
            for j in range(i+1,m):
                if score[j][k]>score[maxx][k]:
                    maxx=j
            score[i],score[maxx]=score[maxx],score[i]
        return score
            


        