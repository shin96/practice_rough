from collections import Counter 

def permutationInAString(string, pattern):
    pattern_memo = Counter(pattern)
    window_start, matched = 0, 0
    for window_end, val in enumerate(string):
        
        if val in pattern_memo:
            pattern_memo[val] -= 1
            if pattern_memo[val] == 0:
                matched += 1
        if matched == len(pattern_memo):
            return True

        if len(string[window_start: window_end + 1]) >= len(pattern):
            if string[window_start] in pattern_memo:
                if pattern_memo[string[window_start]] == 0:
                    matched -= 1
                pattern_memo[string[window_start]] += 1
            window_start += 1
    return False


print(permutationInAString("oidbcaf", "abc"))