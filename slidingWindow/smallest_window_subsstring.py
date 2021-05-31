# Smallest Window containing Substring (hard) #
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

from collections import Counter
def smallestSubsString(string, pattern): 
    char_freq = Counter(pattern)
    window_start, matched, sub_str_start = 0, 0, 0
    min_len = len(string) + 1
    for window_end, val in enumerate(string):
        if val in char_freq:
            char_freq[val] -= 1
            if char_freq[val] >= 0:
                matched += 1
        
        while matched == len(pattern):
            if min_len > window_end - window_start + 1:
                min_len = len(string[window_start: window_end + 1])
                sub_str_start = window_start
            left_char = string[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
    if min_len > len(string):
        return ""
    return string[sub_str_start: sub_str_start + min_len]

print(smallestSubsString("aabdec", "abc"))    

