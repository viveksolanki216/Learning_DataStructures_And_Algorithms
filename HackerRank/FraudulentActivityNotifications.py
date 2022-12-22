# Learning_DataStructures_And_Algorithms
# Date: 2022/Dec/22
# Code By: Vivek Singh Solanki
# Things Learned:

#-------------------------- Top Solution -----------------------------#
# Using Counting Sort, running time complexity O(n*200), (n = 2*10^5)
def get_median(counts, d):
    is_d_odd = d % 2

    if is_d_odd:
        median_i = [int(d / 2)+1]
    else:
        median_i = [int(d / 2), int(d / 2)+1]

    sum = 0
    flag = 0
    for i in range(0, len(counts)):
        sum += counts[i]
        if flag == 0 and sum >= median_i[0]:
            median = i
            flag = 1
        if len(median_i) == 2 and flag == 1 and sum >= median_i[1]:
            median += i
            median *= 0.5
            break
    return median

def activityNotifications(expenditure, d):
    counts = [0] * 10

    for i in range(0, d):
        counts[expenditure[i]] += 1

    count = 0
    # Write your code here
    for i in range(d, len(expenditure)):
        #print(counts)
        median = get_median(counts, d)
        #print(median, ' <= 2*', expenditure[i])
        if expenditure[i] >= 2 * median:
            count += 1
        #print(count)
        counts[expenditure[i -d]] -= 1
        counts[expenditure[i]] += 1
    return count

expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 1
activityNotifications(expenditure, d)

#-------------------------- Worst Solution -----------------------------#
# Brute-Force approach, (n-d)*d*log d approach
def get_median(arr):
    d = len(arr)
    is_d_odd = d % 2
    if is_d_odd:
        median = arr[int(d / 2)]
    else:
        median = 0.5 * (arr[int(d / 2) - 1] + arr[int(d / 2)])
    return median

def activityNotifications(expenditure, d):
    count = 0
    # Write your code here
    for i in range(d, len(expenditure)):
        exp_last_d = expenditure[i - d:i]
        exp_last_d.sort()
        if expenditure[i] >= 2 * get_median(exp_last_d):
            count += 1

    return count
