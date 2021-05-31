# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

from collections import Counter


def longestSubString(string, k):
    memo = {}
    window_start = 0
    count = 0
    max_len = 0
    string_ = ''
    prev_max = max_len

    for window_end, char in enumerate(string):
        if char not in memo:
            memo[char] = 0
        memo[char] += 1

        while len(memo) > k:
            memo[string[window_start]] -= 1
            if memo.get(string[window_start], None) == 0:
                del memo[string[window_start]]
            window_start += 1

        max_len = max(max_len, len(string[window_start: window_end + 1]))
        if prev_max < max_len:
            prev_max = max_len
            string_ = string[window_start: window_end + 1]
    return max_len, string_


print(longestSubString("araaci", 2))
