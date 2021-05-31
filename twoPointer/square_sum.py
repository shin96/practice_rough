# Problem Statement #
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def squateIt(arr):
    arr_size = len(arr)
    result = [None] * arr_size
    input_ptr = arr_size - 1
    start, last = 0, arr_size - 1
    while start <= last:
        start_sq = arr[start] ** 2
        last_sq = arr[last] ** 2
        if start_sq > last_sq:
            result[input_ptr] = start_sq
            start += 1
        else:
            result[input_ptr] = last_sq
            last -= 1
        input_ptr -= 1
    return result

print(squateIt([-3, -1, 0, 1, 2]))