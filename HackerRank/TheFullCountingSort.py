
def countSort(arr):
    # Write your code here
    count_arr = [0] * 100
    dict1 = {}
    mid = len(arr)/2
    i = 0
    for ele, string in arr:
        count_arr[int(ele)] += 1
        if i < mid:
            string = '-'
        if ele in dict1:
            dict1[ele] += [string]
        else:
            dict1[ele] = [string]
        i = i+ 1

    # print(dict1)
    for i in range(100):
        for j in range(count_arr[i]):
            print(dict1[str(i)][j], end=' ')