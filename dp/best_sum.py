# WAF that takess in a number and an array of numbers
# the function should return an array of any combination which sums up to targetSum
# length should be minimum


def best_sum(target_sum, nums, memo = {}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None
    shortest_arr = None

    for num in nums:
        remainder_sum = target_sum - num
        sum_arr = best_sum(remainder_sum, nums, memo)
        
        if sum_arr != None:
            sum_arr.append(num)
            sum_arr += [num]
            if shortest_arr == None or len(sum_arr) < len(shortest_arr):
                shortest_arr = sum_arr
    
    memo[target_sum] = shortest_arr
    return memo[target_sum]


def main():
    print(best_sum(10, [5, 2, 1 ]))


if __name__ == '__main__':
    main()