# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        c = head
        while c:
            if c in d:
                return True
            d[c] = True
            c = c.next
        return False
        