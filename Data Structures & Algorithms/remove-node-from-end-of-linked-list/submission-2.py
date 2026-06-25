# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findl(self,head):
        l=0
        while head:
            l+=1
            head=head.next
        return l

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=self.findl(head)
        dummy=ListNode(0,head)
        print(l)
        if n>l:
            return head
        temp=dummy
        
        for i in range(l-n):
            temp=temp.next  #Moving till n-l+1th element

        temp.next=temp.next.next
        return dummy.next


        

        


        