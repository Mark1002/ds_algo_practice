class Union:

    def __init__(self) -> None:
        self.m = {}

    def find(self, a: int) -> int:
        """找到a背後最大的老大"""

        # root condition
        if self.m.get(a) is None:
            self.m[a] = a
            return a

        manager = self.m[a]
        if a != manager:
            self.m[a] = self.find(manager)  # 升職扁平化
            return self.m[a]
            # return self.find(manager)
        else:
            return a

    def union(self, a: int, b: int):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            print("root_a == root_b")
            return
        self.m[root_a] = root_b


if __name__ == "__main__":

    u = Union()
    u.union(1, 2)
    u.union(3, 4)
    assert u.find(1) == u.find(2)
    assert u.find(2) != u.find(4)
    u.union(1, 3)
    assert u.find(2) == u.find(4)
