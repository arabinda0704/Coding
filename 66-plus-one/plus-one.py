class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=digits
        for i in range(len(s)-1,-1,-1):
    
            if s[i] != 9:
                s[i] += 1  
                break  
            else:
                s[i] = 0
        s=s[::-1]
        if s[-1] == 0:
            s.append(1)

        return s[::-1]
        