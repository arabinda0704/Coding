class Solution:
    def removeStars(self, s: str) -> str:
        #O(N) Time and Space Complexity
        # st=[]
        # for c in s:
        #     if c =="*":
        #         st.pop()
        #     else:
        #         st.append(c)
        # return "".join(st)
        #More Optimal O(N) time and O(1) or O(1) Space
        l = 0
        s = list(s)

        for r in range(len(s)):
            if s[r] == '*':
                l -= 1
            else:
                s[l] = s[r]
                l += 1
                
        return ''.join(s[:l])
        