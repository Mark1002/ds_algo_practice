"""
Merge sort implement.
ref: https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture2.pdf
"""

def merge_sort(a: list) -> list:
    """Merge sort."""
    n = len(a)
    if n <= 1:
        return a
    l = merge_sort(a[:n//2])
    r = merge_sort(a[n//2:])
    return merge(l, r)


def merge(l:list, r:list) -> list:
    """Merge two list."""
    m = len(l) + len(r)
    s = [None] * m
    # add infinite number to prevent exception
    inf = float("inf")
    l.append(inf)
    r.append(inf)
    i, j = 0, 0
    for k in range(m):
        if l[i] <= r[j]:
            s[k] = l[i]
            i += 1  # can be out of range, need add one inf element
        else:
            s[k] = r[j]
            j += 1
    return s


def main():
    """Main."""
    a = [5, 2, 4, 7, 1, 3, 2, 6]
    result = merge_sort(a)
    print(result)


if __name__ == "__main__":
    main()
