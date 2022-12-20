# Learning_DataStructures_And_Algorithms
# Date: 2022/Dec/09
# Code By: Vivek Singh Solanki

# Things Learned:
    # Inserting a element in list on position i : O(n) time complexity
    # String is immutable object
        # So insertion is done through concatenation
        # now imagine inserting n elements in a empty string will be of time O(n^2)
        # At every insertion you have to move n-1 items.
        # So its always better to create a list of characters from string
            # as lst = [*string]
            # or looping over the characters in string.

def biggerIsGreater(w):
    # Convert string to list
    w1 = [*w]
    temp_lst = [w1[len(w1)-1]]
    # Scan list in reverse
    flag = 0
    for i in range(len(w1) - 2, -1, -1):
        #print(i, w1[i])
        j = 0
        while True:
            #print(i, j, w1[i], temp_lst[j])
            if w1[i] < temp_lst[j]:
                flag = 1
                break
            else:
                j += 1
                if j == len(temp_lst):
                    temp_lst.append(w1[i])
                    break
        if flag == 1:
            break

    if flag == 1:
        char_piv = temp_lst[j]
        temp_lst[j] = w1[i]
        final_string = w1[:i] + [char_piv] + temp_lst
        final_string = ''.join(final_string)
    else:
        final_string = 'no answer'

    return final_string

biggerIsGreater('fedcbabcd')










