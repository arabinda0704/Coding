class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Brute Force and will give "Time Limit Exceeded"
        # res=[]
        # for i in range(len(temperatures)):
        #     count=1
        #     j=i+1
        #     while j<len(temperatures):
        #         if temperatures[j]>temperatures[i]:
        #             break
        #         count+=1
        #         j+=1
        #     if j==len(temperatures):
        #         count=0
        #     res.append(count)
        # return res

        #Optimal

        res=[0]*len(temperatures)
        st=[] # pair: [temp, index]
        for i,t in enumerate(temperatures):
            while st and t>st[-1][0]:
                temp,ind=st.pop()
                res[ind]=(i-ind)
            st.append((t,i))
        return res
            



        