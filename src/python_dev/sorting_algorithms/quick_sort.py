def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)
    return A


def quick_sort2(A, low, high):
    if low < high:
        p = partition(A, low, high)
        quick_sort2(A, low, p-1)
        quick_sort2(A, p+1, high)


def get_pivot(A, low, high):
    mid = (low + high) // 2
    pivot = high
    if A[low] < A[mid]:
        if A[mid] < A[high]:
            pivot = mid
    elif A[low] < A[high]:
        pivot = low
    return pivot


def partition(A, low, high):
    pivotindex = get_pivot(A, low, high)
    pivotvalue = A[pivotindex]
    A[pivotindex], A[low] = A[low], A[pivotindex]
    border = low
    for i in range(low, high+1):
        if pivotvalue > A[i]:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]
    return (border)


the_list = [9, 8, 3, 7, 1, 0, 5]
print("Original list: ", the_list)
print("Sorted list: ", quick_sort(the_list))
