# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        temp=list1
        while b:
            temp=temp.next
            b-=1
        bthNode=temp.next
        temp1=list1
        while a-1:
            temp1=temp1.next
            a-=1
        athnode=temp1
        temp2=list2
        while temp2.next:
            temp2=temp2.next
        temp2.next=bthNode
        athnode.next=list2
        return list1
        



        