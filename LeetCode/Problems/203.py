# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ans = ListNode()
        cur = ans
        while head:
            if head.val != val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        return ans.next