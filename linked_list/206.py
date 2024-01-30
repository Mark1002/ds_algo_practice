"""
https://leetcode.com/problems/reverse-linked-list/
"""
from typing import Optional

from utils import run


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        if cur is None:
            return head
        while cur.next:
            n = cur.next
            cur.next = n.next
            n.next = head
            head = n
        return head


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": "", "ans": ""},
    ]
    run(test_cases, s.reverseList)
