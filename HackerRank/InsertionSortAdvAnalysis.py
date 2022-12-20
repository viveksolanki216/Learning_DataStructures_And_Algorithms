# Learning_DataStructures_And_Algorithms
# Date: 2022/Dec/15
# Code By: Vivek Singh Solanki
# Objective: Count the number of shifts in the insertion sort
# Things Learned:

# O(n^2), Solution
def sort_shift_counter(arr):
    # Write your code here
    count = 0
    for i in range(1,len(arr)):
        key = arr[i]
        for j in range(i-1, -1, -1):
            if key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
                count += 1
            else:
                break
        arr[j+1] = key
    print(arr)
    return count

sort_shift_counter([3,4,7,5,6,2,1])

insertionSort2(7, [3,4,7,5,6,2,1])


def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print(*arr, sep=' ')

# O(nlon) solution

def sort_shift_counter(arr):
    # Recursion termination condition
    #print(len(arr))
    if len(arr) == 1:
        return 0
    # Call Recursuion
    mid = len(arr)//2
    L = arr[0:mid]
    R = arr[mid:len(arr)]
    count_l = sort_shift_counter(L)
    count_r = sort_shift_counter(R)

    # Merge Sort
    i = j = k = 0
    len_left_arr = len(L)
    count = count_r + count_l
    while( i < len(L) and j < len(R) ):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
            count += len_left_arr + j - k

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return count

count = sort_shift_counter([4, 8, 1, 7, 5, 3, 2])
print(count)

