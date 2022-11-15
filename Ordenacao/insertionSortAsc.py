def insertionSortAsc(A):
    
    for i in range(1, len(A)):
        key = A[i]
        j = i -1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key

    return A 

A = [31, 41, 59, 62, 42, 58]

print(insertionSortAsc(A))