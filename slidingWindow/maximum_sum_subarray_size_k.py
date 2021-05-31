# Given an array of positive numbers and a positive number ‘k’, 
# find the maximum sum of any contiguous subarray of size ‘k’.
# Example 1:
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

def findWindowOfMaxSum(arr, k):
    window_start, prev_max_sum, max_sum, window_sum = 0, 0, 0, 0
    result = []
    pos = [0, 0]
    for window_end, ele in enumerate(arr):
        window_sum += ele
        if window_end >= k - 1:
            max_sum = max(window_sum, max_sum)
            if (prev_max_sum < max_sum):
                pos[0] = window_start
                pos[1] = window_end
                prev_max_sum = max_sum
            window_sum -= arr[window_start]
            window_start += 1
    return (max_sum, arr[pos[0]:pos[1]+1])

print(findWindowOfMaxSum([2, 1, 5, 1, 3, 2], 3))
