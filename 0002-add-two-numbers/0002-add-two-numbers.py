# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(0)
        tailpointer=dummynode
        reminder=0
        while l1 or l2 or reminder:
            value1=l1.val if l1 else 0
            value2=l2.val if l2 else 0
            
            add=value1+value2 +reminder
            reminder =add//10
            add=add%10
            newNode=ListNode(add)
            tailpointer.next=newNode
            tailpointer=tailpointer.next
            
            
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
            
        result=dummynode.next
        dummynode.next=None
        return result
            
            
        