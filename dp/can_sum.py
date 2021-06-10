# WAF that takess in a number and an array of numbers
# the function will return if the number can be used to calculate the 
# target sum or not


def can_sum(target_sum, nums, memo = {}):
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return True
    if target_sum < 0: return False
    
    for num in nums:
        required_sum = target_sum - num
        if can_sum(required_sum, nums, memo):
            memo[target_sum] = True
            return True
    
        memo[target_sum] = False
        return False




def main():
    print(can_sum(300, [7,4]))


if __name__ == '__main__':
    main()