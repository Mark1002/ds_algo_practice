"""
url: https://leetcode.com/problems/add-two-numbers
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        v1 = self.trace_sum(l1)
        v2 = self.trace_sum(l2)
        total = v1 + v2
        return self.convert_linked_list(total)

    def convert_linked_list(self, number: int) -> ListNode:
        head = None
        for digit in str(number):
            head = ListNode(int(digit), head)
        return head

    def trace_sum(self, node: ListNode) -> int:
        if node is None:
            return 0
        else:
            return node.val + 10 * self.trace_sum(node.next)


if __name__ == "__main__":
    s = Solution()
    l3 = s.addTwoNumbers(
        l1=s.convert_linked_list(342),
        l2=s.convert_linked_list(465)
    )
    print(s.trace_sum(l3))
