"""
two pointers technique: 
given a sorted array, one side is the leftmost pointer,
the other side is the rightmost pointer.
we can use these two pointers to compare or search element.
"""

def is_pair_sum(arr: list, val:int) -> bool:
    arr.sort()
    left, right = 0, len(arr)-1
    while left < right:
        total = arr[left] + arr[right]
        if total == val:
            return True
        if total < val:
            left += 1
        if total > val:
            right -= 1
    return 0


if __name__ == "__main__":
    arr = [3, 5, 9, 2, 8, 10, 11]
    val = 17
    print(is_pair_sum(arr, val))
