"""https://leetcode.com/problems/task-scheduler/."""
import heapq
from typing import List
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # construct max heap by task frequency
        task_freq = Counter(tasks)
        heap_q = [-freq for freq in task_freq.values()]
        heapq.heapify(heap_q)
        # temp q for task to wait cpu interval
        temp_q = deque()
        time = 0

        while heap_q or temp_q:
            time += 1
            if heap_q:
                freq = heapq.heappop(heap_q)
                freq += 1  # task freq decrease 1
                if freq:
                    wakeup_time = time + n  # the task next wake up time
                    temp_q.append((freq, wakeup_time))
            # task wake up and resume to priority queue
            if temp_q and time == temp_q[0][1]:
                freq, _, = temp_q.popleft()
                heapq.heappush(heap_q, freq)
        return time
