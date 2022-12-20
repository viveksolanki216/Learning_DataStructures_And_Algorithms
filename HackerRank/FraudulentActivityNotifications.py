
def activityNotifications(expenditure, d):
    is_d_odd = d % 2
    count = 0
    # Write your code here
    for i in range(d ,len(expenditure)):
        exp_last_d = expenditure[ i -d:i]
        exp_last_d.sort()
        if is_d_odd:
            median = exp_last_d[int( d /2)]
        else:
            median = 0.5 *(exp_last_d[int(d / 2) - 1] + exp_last_d[int(d / 2)])
        if expenditure[i] >= 2 * median:
            count += 1

    return count