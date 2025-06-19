class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        operators="+-/*"
        for i in range(len(tokens)):
            if tokens[i] in operators:
                op1=st.pop()
                op2=st.pop()
                if tokens[i]=="+":
                    st.append(op1+op2)
                if tokens[i]=="-":
                    st.append(op2-op1)
                if tokens[i]=="/":
                    st.append(int(op2/op1))
                if tokens[i]=="*":
                    st.append(op1*op2)
    
            else:
                st.append(int(tokens[i]))
        return st.pop() #st[0] or st[-1] or st.pop() are same here because st will contain exactly one element at the end
                

        