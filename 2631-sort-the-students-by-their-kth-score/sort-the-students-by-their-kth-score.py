class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        if len(score)==1:
            return score
        m=len(score)
        n=len(score[0])
        for i in range(m):
            max_index = i
            for j in range(i + 1, m):
                if score[j][k] > score[max_index][k]:
                    max_index = j
            
            score[i], score[max_index] = score[max_index], score[i]
        
        return score
            


        