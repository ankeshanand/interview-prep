"""
* Implementation of Hoare and Lomuto Array Partitiioning scheme.
* Implementation of the quickselect algorithm to find the Kth smallest
element in an array.
"""


def hoare_partition(A, pivot_index):
    pivot = A[pivot_index]
    A[0], A[pivot_index] = A[pivot_index], A[0]
    left_ptr, right_ptr = -1, len(A)

    while True:
        while True:
            left_ptr += 1
            if A[left_ptr] >= pivot:
                break
        while True:
            right_ptr -= 1
            if A[right_ptr] <= pivot:
                break

        if left_ptr < right_ptr:
            print A, left_ptr, right_ptr
            A[left_ptr], A[right_ptr] = A[right_ptr], A[left_ptr]
        else:
            return right_ptr


def lomuto_partition(A, pivot_index):
    pivot = A[pivot_index]
    A[-1], A[pivot_index] = A[pivot_index], A[-1]
    pivot_pos = -1
    for i, item in enumerate(A[:-1]):
        if item <= pivot:
            pivot_pos += 1
            A[pivot_pos], A[i] = A[i], A[pivot_pos]
    pivot_pos += 1
    A[-1], A[pivot_pos] = A[pivot_pos], A[-1]
    # print "Array after partitioning: " + str(A)
    # print "Final pivot position: " + str(pivot_pos)
    return pivot_pos


def quickselect(A, k):
    """
    Find the kth smallest (zero indexed) number in A.
    """
    pivot_pos = lomuto_partition(A, 0)
    print A, pivot_pos, k
    if k == pivot_pos:
        return A[pivot_pos]
    if k < pivot_pos:
        return quickselect(A[:pivot_pos], k)
    else:
        return quickselect(A[pivot_pos+1:], k-pivot_pos-1)

if __name__ == "__main__":
    A = [3, 1, 1, 2, 6, 0]
    B, C = A[:], A[:]
    pivot_pos = hoare_partition(A, 1)
    # print pivot_pos
    pivot_pos = lomuto_partition(B, 1)
    # print pivot_pos
    kth_smallest = quickselect(C, 3)
    print kth_smallest
