
#

arr = [4,3,2,1]
mergeSort(arr)
print(arr)

def mergeSort(arr):
    # Recursion termination condition
    #print(len(arr))
    if len(arr) == 1:
        return
    # Call Recursuion
    mid = len(arr)//2
    L = arr[0:mid]
    R = arr[mid:len(arr)]
    mergeSort(L)
    mergeSort(R)

    # Merge Sort
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return
