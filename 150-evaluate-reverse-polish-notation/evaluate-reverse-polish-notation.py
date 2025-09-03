class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        operators="+-/*"
        for i in range(len(tokens)):
            if tokens[i] in operators:
                a2=int(st.pop())
                a1=int(st.pop())
                if tokens[i]=="+":
                    st.append(a1+a2)
                elif tokens[i]=="-":
                    st.append(a1-a2)
                elif tokens[i]=="/":
                    st.append(int(a1/a2))
                else:
                    st.append(a1*a2)

            else:
                st.append(int(tokens[i]))
        return st[0]
        