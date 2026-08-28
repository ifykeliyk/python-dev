def selection_sort(A):
    for i in range(0, len(A)-1):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
    return A


the_list = [9, 8, 6, 1, 4, 7, 5]

print("Original list: ", the_list)
print("Sorted list: ", selection_sort(the_list))
