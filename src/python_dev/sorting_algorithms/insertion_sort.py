def insertion_sort(A):
    for i in range(1, len(A)):
        curnum = A[i]
        for j in range(i-1, -1, -1):
            if A[j] > curnum:
                A[j+1] = A[j]
                A[j] = curnum
            else:
                A[j+1] = curnum
                break
    return A


the_list = [9, 8, 4, 0, 2, 3, 7]

print("Original list: ", the_list)
print("Sorted list: ", insertion_sort(the_list))
