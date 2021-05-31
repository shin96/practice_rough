def dutch_flag_sort(arr):
    zero, one, two = 0, 0, len(arr) - 1
    while one <= two :
        if arr[one] == 0:
            arr[zero], arr[one] = arr[one], arr[zero]
            zero += 1
            one += 1
        elif arr[one] == 1:
            one += 1
        else:
            arr[one], arr[two] = arr[two], arr[one]
            two -= 1
    # return arr

arr = [1, 0, 2, 1, 0]
dutch_flag_sort(arr)
print(arr)
# print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
