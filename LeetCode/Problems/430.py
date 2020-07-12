"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        st, cur = [], head
        while cur or len(st):
            if cur.child:
                if cur.next: st.append(cur.next)
                cur.next = cur.child
                cur.next.prev = cur
                cur.child = None
            else:
                if not cur.next and len(st):
                    cur.next = st.pop()
                    cur.next.prev = cur
            cur = cur.next
        return head