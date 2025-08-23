# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr =head
        n=0
        while curr:
            curr=curr.next
            n+=1

        nge = [0] * n
        st = []
        nums=[]
        temp=head
        while temp:
            nums.append(temp.val)
            temp=temp.next
        for i in range(n-1,-1,-1):
            while st and st[-1] <= nums[i % n]:
                st.pop()


            if i < n:
                if st:
                    nge[i] = st[-1]
            st.append(nums[i % n])
        return nge

        
        
        
        