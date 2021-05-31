# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
#aaaabcd
def longestSubStringWithSameLetter(string, k):
    memo = {}
    window_start, max_len = 0, 0 
    most_repeated_char = 0
    for window_end, char in enumerate(string):
        if char not in memo:
            memo[char] = 0
        memo[char] += 1

        most_repeated_char = max(most_repeated_char, memo[char])
        non_repeated_chars = len(string[window_start: window_end + 1]) - most_repeated_char 

        if non_repeated_chars > k:
            memo[string[window_start]] -= 1
            window_start += 1
        max_len = max(max_len, len(string[window_start: window_end + 1]))
    return max_len
        
print(longestSubStringWithSameLetter("abccde", 1))


