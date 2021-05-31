def runningSum(nums):
        result = [nums[0]]
        
        if (len(nums) == 1): 
            return nums
        print(result[0], "result")
        for ind, ele in enumerate(nums[1:]):
            print(ele, ind)
            res = result[ind] + ele
            result.append(res)
        return result

print(runningSum([1,2,3,4]))