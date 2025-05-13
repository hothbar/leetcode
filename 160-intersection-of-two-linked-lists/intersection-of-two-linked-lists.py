# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        nodeA = headA
        nodeB = headB

        while nodeA and nodeB:
            if nodeA in s:
                return nodeA
            s.add(nodeA)
            if nodeB in s:
                return nodeB
            
            s.add(nodeB)

            nodeA = nodeA.next
            nodeB = nodeB.next

        while nodeA:
            if nodeA in s:
                return nodeA
            s.add(nodeA)
            nodeA = nodeA.next

        while nodeB:
            if nodeB in s:
                return nodeB
            s.add(nodeB)
            nodeB = nodeB.next

        return None