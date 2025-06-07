class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s=digits
        # for i in range(len(s)-1,-1,-1):
        #     if s[i]==9:
        #         s[i] = 0
        #     else:
        #         s[i] += 1  
        #         # return s #This line is not mandatory
        #         break  
        # # s=s[::-1]
        # # if s[-1] == 0:
        # #     s.append(1)

        # # return s[::-1]
        # if s[0]==0:   #As the question suggest that question will not contain any leading 0's
        #     s.insert(0, 1)
        # return s
        #Another good approach
        s=digits
        for i in range(len(s)-1,-1,-1):
            if s[i]==9:
                s[i] = 0
            else:
                s[i] += 1  
                return s
        s.insert(0, 1) #As the question suggest that question will not contain any leading 0's
        return s