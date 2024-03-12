# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode(0)
        currentpointer=dummyNode
        reminder=0
        while l1 or l2 or reminder:
            link1=l1.val if l1 else 0
            link2=l2.val if l2 else 0
            sumlink=link1+link2+reminder
           
            reminder=sumlink//10
            sumlink=sumlink%10
            newnode=ListNode(sumlink)
            currentpointer.next =newnode
            currentpointer=currentpointer.next
            
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        result =dummyNode.next
        dummyNode.next =None
        return result
            
            

            
          
            
            
            
        