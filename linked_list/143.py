"""
https://leetcode.com/problems/reorder-list/description/
"""
from typing import Optional, List

from utils import run


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_list(nodes: List[ListNode]) -> ListNode:
    if len(nodes) == 0:
        return None
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0]


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None or head.next.next is None:
            return
        # Find middle node
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse last part
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # Merge two linked lists
        l1 = head
        l2 = prev
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            l1 = temp1
            l2 = temp2

        cur = head
        while cur:
            print(cur.val)
            cur = cur.next


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {
                "head": linked_list([
                    ListNode(1),
                    ListNode(2),
                    ListNode(3),
                    ListNode(4),
                    ListNode(5),
                    ListNode(6),
                    ListNode(7),
                ])
            },
            "ans": None
        },
    ]
    run(test_cases, s.reorderList)
