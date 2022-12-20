
# Learning_DataStructures_And_Algorithms: Big Sorting
# Date: 2022/Dec/18
# Code By: Vivek Singh Solanki

# Attempt 1: Failed, Because following solution is converting big string to int that takes theta(n^2) time for n digits
def bigSorting(unsorted):
    # Write your code here
    arr = [int(ele) for ele in unsorted]
    arr.sort()
    arr = [str(ele) for ele in arr]
    return arr

# Attempt 2: Crux is convert strings into digits when its necessary, when they are of equal lenghts and then convert
# it to change it to interger to compare to sort.

arr = ['4','3','2','1000000000000000000']
mergeSort(arr)
print(arr)

def bigSorting(arr):
    # Recursion termination condition
    #print(len(arr))
    if len(arr) == 1:
        return arr
    # Call Recursuion
    mid = len(arr)//2
    L = arr[0:mid]
    R = arr[mid:len(arr)]
    L = bigSorting(L)
    R = bigSorting(R)

    # Merge Sort
    i = j = k = 0
    while i < len(L) and j < len(R):
        if len(L[i]) < len(R[j]):
            arr[k] = L[i]
            i += 1
            k += 1
        elif len(L[i]) > len(R[j]):
            arr[k] = R[j]
            j += 1
            k += 1
        else:
            if int(L[i]) <= int(R[j]):
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

    return arr
