from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def _print(self):
        curr = self
        while curr:
            print(curr.val)
            curr = curr.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result = ListNode()
        odd = 0 
        while l1 or l2 or odd:
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            sum = val1 + val2 + odd
            mod, res = divmod(sum, 10)
            dummy.next = ListNode(res)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next
    

addTwoNumbers = Solution().addTwoNumbers

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)

result._print()
