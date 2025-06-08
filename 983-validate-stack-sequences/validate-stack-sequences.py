class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        j = 0  # pointer for popped
        for x in pushed:
            st.append(x)
            while st and j < len(popped) and st[-1] == popped[j]:
                st.pop()
                j += 1
        return not st
        