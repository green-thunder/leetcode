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
        l1_cr = l1
        l2_cr = l2
        result = ListNode()
        dummy = result
        odd = 0 
        while l1_cr and l2_cr:
            sum = l1_cr.val + l2_cr.val + odd
            odd = sum//10
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
            l1_cr = l1_cr.next
            l2_cr = l2_cr.next
        
        while l1_cr:
            sum = l1_cr.val + odd
            odd = sum // 10
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
            l1_cr = l1_cr.next

        while l2_cr:
            sum = l2_cr.val + odd
            odd = sum // 10
            dummy.next = ListNode(sum%10)
            dummy = dummy.next
            l2_cr = l2_cr.next
        
        if odd:
            dummy.next = ListNode(odd)

        return result.next
    

addTwoNumbers = Solution().addTwoNumbers

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = addTwoNumbers(l1, l2)

result._print()
