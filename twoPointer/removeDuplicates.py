# Problem Statement #
# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def removeDuplicates(array):
    prev_ind = 1
    for cur_ind in range(len(array)):
        if array[prev_ind - 1] != array[cur_ind]:
            array[prev_ind] = array[cur_ind]
            prev_ind += 1
            
    return (prev_ind, array[:prev_ind])

print(removeDuplicates([2, 3, 3, 3, 6, 9, 9]))