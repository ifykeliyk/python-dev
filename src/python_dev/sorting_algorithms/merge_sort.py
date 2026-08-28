def merge_sort(A):
    merge_sort2(A, 0, len(A)-1)
    return A


def merge_sort2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle+1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle+1]
    R = A[middle+1:last+1]
    L.append(99999999)
    R.append(99999999)
    i = j = 0
    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


the_list = [3, 9, 0, 6, 8, 4, 1]
print("Original list: ", the_list)
print("Sorted list: ", merge_sort(the_list))
