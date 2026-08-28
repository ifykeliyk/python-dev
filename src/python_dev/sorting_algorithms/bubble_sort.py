def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A


thelist = [9, 2, 3, 5, 7, 6, 1, 0]
print("Original list: ", thelist)
print("Sorted list: ", (bubble_sort(thelist)))
