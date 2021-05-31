def tripletSmallerThanTarget(arr, target):
    arr.sort()
    arr_size = len(arr)
    count = 0
    for i in range(arr_size - 2):
        left = i + 1
        right = arr_size - 1
        while left < right: 
            target_diff = arr[i] + arr[left] + arr[right]
            if target_diff < target:
                count += right - left
                left += 1
            
            if target_diff >= target:
                right -= 1
    return count

print(tripletSmallerThanTarget([-1, 4, 2, 1 ,3 ], 5))