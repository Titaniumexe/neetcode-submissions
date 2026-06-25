class Solution:
    def reversalll(self, head):
        nextt, curr = head, head
        prev = None
        while curr:
            nextt = nextt.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
    
    def findl(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = self.findl(head)
        if k > l:
            return head
        
        # 1. Advance to the end of the current k-group
        curr = head
        for i in range(k - 1):  # Stopped at k-1 to keep reference to the group tail
            curr = curr.next
        
        # 2. Store the start of the remaining list
        remaining_list = curr.next
        curr.next = None  # Cut off the first k-group

        # 3. Reverse the first k-group exactly once
        l1 = self.reversalll(head)
        
        # 4. Recursively process the rest of the list
        l2 = self.reverseKGroup(remaining_list, k)

        # 5. Connect the tail of the reversed group (which is 'head') to the rest
        head.next = l2

        return l1
