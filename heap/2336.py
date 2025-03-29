"""https://leetcode.com/problems/smallest-number-in-infinite-set."""
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.heap = []  # only add num from addBack
        self.hm = set()  # only record num smaller than smallest

    def popSmallest(self) -> int:
        if self.heap:
            cur_smallest = heapq.heappop(self.heap)
            self.hm.remove(cur_smallest)
            return cur_smallest
        cur_smallest = self.smallest
        self.smallest += 1
        return cur_smallest

    def addBack(self, num: int) -> None:
        # return if num aleady in heap
        if num in self.hm or num >= self.smallest:
            return
        heapq.heappush(self.heap, num)
        self.hm.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
