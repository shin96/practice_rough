# Words Concatenation (hard) #
# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

# Example 1:

# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Example 2:

# Input: String="catcatfoxfox", Words=["cat", "fox"]
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".

from collections import Counter 
def wordConcat(string, words):
    len_of_word = len(words[0])
    word_count = len(words)
    word_freq = Counter(words)
    result = []

    for i in range((len(string) - word_count * len_of_word) + 1):
        word_seen = {}
        for j in range(word_count):
            next_word_indx = i + j * len_of_word
            word = string[next_word_indx: next_word_indx + len_of_word]
            if word not in word_freq:
                break

            if word not in word_seen:
                word_seen[word] = 0
            word_seen[word] += 1

            if word_seen[word] > word_freq.get(word, 0):
                break
            if j + 1 == word_count:
                result.append(i)
    return result

