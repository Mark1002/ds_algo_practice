"""https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list."""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s = f = head
        # s point to the middle node
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        # reverse the right part
        cur = s.next
        s.next = None
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        l, r = head, prev
        result = 0
        while l and r:
            result = max(l.val + r.val, result)
            l = l.next
            r = r.next
        return result
