# WAF that takess in a number and an array of numbers
# the function should return an array of any combination which sums up to targetSum


def how_sum(target_sum, nums, memo = {}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    for num in nums:
        remainder_sum = target_sum - num
        sum_arr = how_sum(remainder_sum, nums, memo)
        if sum_arr != None:
            sum_arr.append(num)
            memo[target_sum] = sum_arr
            return memo[target_sum]
    memo[target_sum] = None
    return memo[target_sum]


def main():
    print(how_sum(300, [7, 14]))


if __name__ == '__main__':
    main()