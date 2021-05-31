# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.


def longestOnes(arr, k):
    window_start, window_size, max_len = 0, 0, 0
    one_count = 0
    for window_end, ele in enumerate(arr):
        if ele == 1:
            one_count += 1
        window_size = len(arr[window_start: window_end + 1])
        zero_count = window_size - one_count
        if zero_count > k:
            if arr[window_start] == 1:
                one_count -= 1
            window_start += 1
        max_len = max(max_len, len(arr[window_start: window_end + 1]))
    return max_len


print(longestOnes([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
