"""https://leetcode.com/problems/lru-cache."""
from typing import Dict


# Double linked list
class ListNode:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.node_num = 0
        self.m: Dict[int, ListNode] = {}
        self.head = ListNode(-1, -1)  # dummy helper node
        self.trail = self.head

    def get(self, key: int) -> int:
        if self.m.get(key):
            # update recently used node order
            self._update_recently_node(key)
            return self.m[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.m.get(key):
            self.m[key].val = value
            # update recently use key
            self._update_recently_node(key)
        elif self.node_num < self.capacity:
            self._add_node(key, value)
        else:
            # remove LRU key
            self._remove_node()
            self._add_node(key, value)

    def _update_recently_node(self, key: int):
        """Update recently used node."""
        node = self.m[key]
        if node is not self.head:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            # add to the front as new head
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node

    def _add_node(self, key: int, value: int):
        node = ListNode(key, value, None, self.head)
        self.head.prev = node
        self.head = node
        self.m[key] = node
        self.node_num += 1

    def _remove_node(self):
        """Remove least recently used node."""
        last_node = self.trail.prev
        self.trail.prev = last_node.prev
        if last_node.prev:
            last_node.prev.next = self.trail
        else:
            self.head = self.trail
        last_node.prev = None
        last_node.next = None
        del self.m[last_node.key]
        self.node_num -= 1
