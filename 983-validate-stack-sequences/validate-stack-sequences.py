class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #O(N) time and space
        # st = []
        # j = 0  # pointer for popped
        # for x in pushed:
        #     st.append(x)
        #     while st and j < len(popped) and st[-1] == popped[j]:
        #         st.pop()
        #         j += 1
        # return not st

        #O(N) time and O(1) space
        l = r = 0
        for num in pushed:
            pushed[l] = num
            l += 1
            while l > 0 and pushed[l - 1] == popped[r]:
                r += 1
                l -= 1
        return l == 0
        