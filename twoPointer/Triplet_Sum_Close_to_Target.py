# Problem Statement #
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

import sys, math

def tripletSumClosestToTarget(arr, target):
    arr.sort()
    smallest_difference = sys.maxsize
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            targetDiff = target - arr[i] - arr[left] - arr[right]
            if targetDiff == 0:
                return target - targetDiff
            
            if abs(targetDiff) < abs(smallest_difference):
                smallest_difference = targetDiff
            
            if targetDiff > 0:
                left += 1
            else:
                right -= 1
    return target - smallest_difference


print(tripletSumClosestToTarget([-3, -1, 1, 2], 2))