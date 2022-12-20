

# Learning_DataStructures_And_Algorithms: ClosestNumbers
# Date: 2022/Dec/18
# Code By: Vivek Singh Solanki

arr = [-20, -3916237, -357920 ,-3620601, 7374819 ,-7330761, 30 ,6246457, -6461594 ,266854]
closestNumbers(arr)

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    diff = [ arr[i+1] - arr[i] for i in range(len(arr)-1)]
    min_diff = min(diff)
    print(min_diff)
    result = []
    for i in range(len(diff)):
        if diff[i] == min_diff:
            result.extend([arr[i], arr[i+1]])
    return result
