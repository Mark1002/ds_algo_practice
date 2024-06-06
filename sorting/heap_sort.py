"""https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture4.pdf"""
from typing import List


def max_heapify(a: List[int], i: int, heap_size: int):
    left = 2 * i + 1
    right = 2 * i + 2
    biggest = i

    if left < heap_size and a[i] < a[left]:
        biggest = left
    if right < heap_size and a[biggest] < a[right]:
        biggest = right
    if biggest != i:
        a[biggest], a[i] = a[i], a[biggest]
        max_heapify(a, biggest, heap_size)


def build_max_heap(a: List[int]):
    last_p = len(a)//2-1
    for i in range(last_p, -1, -1):
        max_heapify(a, i, len(a))


def heap_sort(a):
    heap_size = len(a)
    build_max_heap(a)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap_size -= 1
        print(heap_size)
        max_heapify(a, 0, heap_size)
    print(f'heap sort: {a}')


if __name__ == "__main__":
    a = [26, 1, 4, 16, 22, 5, 33]
    heap_sort(a)
