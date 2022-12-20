

# Problem 1: Quicksort 1- Partition

# What Learned:
    # Its a comparison sort. And a comparison sort algoritm cannot beat n * log(n) running time.
    # Quick sort is also called partition sort
    # Genarally leftmost item is considered pivot, that causes worst case behaviour on the already sorted arrays.
        # so random pivot can be chosen.
    # Different partition algoithms also exists.


# Quicksort 1 - Partition
# Creare a function that parition an array into three sub-arrays, left, equal and right, where each element in left < pivot,
# each element in right is > pivot and each elemnt in equal =p.

def partiotion(arr):
    # Write your code here
    pivot = arr[0]
    p = l = 0
    r = len(arr)-1
    while l <= r:
        if arr[l] < pivot:
            arr[l], arr[p] = arr[p], arr[l]
            l += 1
            p += 1
        elif arr[l] > pivot:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
        else: # when arr[l] == pivot
            l += 1
    return arr
