# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

#abacdef

def longestSubString(string):
    memo = {}
    window_start = 0
    max_len = 0
    for window_end, val in enumerate(string):
        if val in memo:
            window_start = max(window_start, memo[val] + 1)
        memo[val] = window_end
        max_len = max(max_len, len(string[window_start: window_end + 1]))
    return max_len

print(longestSubString("abccde"))

        
