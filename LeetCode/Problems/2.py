# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = 0
        mul = 1
        while l1:
            res += l1.val * mul
            mul *= 10
            l1 = l1.next
        mul = 1
        while l2:
            res += l2.val * mul
            mul *= 10
            l2 = l2.next
        ans = ListNode(res % 10)
        cur = ans
        while res >= 10:
            res //= 10
            cur.next = ListNode(res % 10)
            cur = cur.next
        return ans
            
        