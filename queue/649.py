from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queueR, queueD = deque(), deque()
        n = len(senate)
        for i, senator in enumerate(senate):
            if senator == "R":
                queueR.append(i)
            else:
                queueD.append(i)
        while queueR and queueD:
            r_i = queueR.popleft()
            d_i = queueD.popleft()
            # 加n表示下一輪的index，不加會導致上一個較小的index永遠還是最小
            if d_i < r_i:
                queueD.append(d_i + n)
            else:
                queueR.append(r_i + n)
        return "Radiant" if queueR else "Dire"
