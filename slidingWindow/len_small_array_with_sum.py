# Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

import sys
def getLenOfSmallSum(arr, s_sum):
    window_start, window_sum = 0, 0
    min_len = sys.maxsize - 1
    for window_end, ele in enumerate(arr):
        window_sum += ele
        if window_sum >= s_sum: 
            min_len = min(min_len, len(arr[window_start: window_end + 1]))
            window_sum -= arr[window_start]
            window_start += 1
    
    if min_len == sys.maxsize - 1: 
        return 0
    return (min_len)

print(getLenOfSmallSum([3, 4, 1, 1, 6], 8 ))