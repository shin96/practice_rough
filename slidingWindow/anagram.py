from collections import Counter

def count_anagram(string, pattern):
    pattern_freq = Counter(pattern)
    window_start, matched = 0, 0
    index = []
    for window_end, val in enumerate(string):

        if val in pattern_freq:
            pattern_freq[val] -= 1
            if pattern_freq[val] == 0:
                matched += 1
        
        if matched == len(pattern):
            index.append(window_start)
        
        if window_end >= len(pattern) - 1:
            if string[window_start] in pattern_freq:
                if pattern_freq[string[window_start]] == 0:
                    matched -= 1
                pattern_freq[string[window_start]] += 1
            window_start += 1
    return index

print(count_anagram("ppqp", "pq"))