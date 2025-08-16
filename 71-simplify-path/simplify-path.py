class Solution:
    def simplifyPath(self, path: str) -> str:
        # st=[]
        # cur=""
        # for c in path+"/":
        #     if c=="/":
        #         if cur=="..":
        #             if st:
        #                 st.pop()
        #         elif cur !="" and cur !=".":
        #             st.append(cur)
        #         cur=""
        #     else:
        #         cur+=c
        # return "/"+"/".join(st)

        #Another
        # st=[]
        # cur=""
        # for c in path+"/":
        #     if c=="/":
        #         if cur==".." and st:
        #             st.pop()
        #         elif cur and cur !="." and cur != "..":
        #             st.append(cur)
        #         cur=""
        #     else:
        #         cur+=c
        # return "/"+"/".join(st)

        #Another After splitting
        tokens=path.split("/")
        st=[]
        for t in tokens:
            if t=="" or t==".":
                continue
            elif t==".." and st:
                st.pop()
            else:
                if t!="..":
                    st.append(t)
        return "/"+"/".join(st)