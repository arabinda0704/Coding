# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first,second,prev=head,head.next,None
        while first and second:
            third=second.next

            second.next=first
            first.next=third
            if prev!=None:
                prev.next=second
            else:
                head=second
            #Updation
            prev=first
            first=third
            if third!=None:
                second=third.next
            else:
                seconde=None
        return head