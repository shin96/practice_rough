def sliding_window(arr, k):
    result = []
    window_start, window_sum = 0, 0
    for window_end, ele in enumerate(arr):
        window_sum += ele
        if window_end >= k - 1:
            result.append(window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return result

print(sliding_window([1,2,2,3,4,5,6,7], 3))