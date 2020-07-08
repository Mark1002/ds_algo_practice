"""Insert sort implement.
ref: https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture1.pdf
"""


def insert_sort(a: list) -> list:
    """Insert sort."""
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            # 比 key 大 往右偏移
            a[i+1] = a[i]
            i-=1
        # 最後一位 replace key
        a[i+1] = key
    return a
            
def main():
    """Main function."""
    a = [5, 2, 4, 6, 1, 3]
    result = insert_sort(a)
    print(result)

if __name__ == "__main__":
    main()
