"""Remove duplicate element."""


def removeDuplicates(A):
    """Inplement."""
    if not A:
        return 0

    newTail = 0

    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1
            A[newTail] = A[i]
            print(f"newTail: {newTail}, i: {i}, {A}")
    return newTail + 1


if __name__ == '__main__':
    removeDuplicates([1, 1, 1, 3, 3, 3, 4, 4, 5, 5])
