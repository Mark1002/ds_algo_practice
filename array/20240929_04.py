"""醫生有 S 個名額，A 跟 B 陣列存放名額號碼。第 Kth 病人可以從 A 或 B 陣列選擇 A[k] or B[k]。
其中名額號碼只能同一給一個病人。
"""

A = [2, 5, 6, 5]
B = [5, 4, 2, 2]

S = 10


def solution(A, B, S):
    if S < len(A):
        return False

    t = []
    d_s = set()
    for a, b in zip(A, B):
        t.append((a, b))
        d_s.add(a)
        d_s.add(b)

    n = 2 ** len(t)
    for i in range(0, n):
        c_s = set()
        s = f"{i:0{len(t)}b}"
        for i, c in enumerate(s):
            j = int(c)
            c_s.add(t[i][j])
            if len(c_s) == len(d_s):
                print(c_s)
                return True
    return False


assert solution(A, B, S) is True
