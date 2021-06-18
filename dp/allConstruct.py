def all_construct(target_word, word_bank, memo = {}):

    if target_word in memo: return memo[target_word]
    if target_word == "": return [[]]
    total_ways = []
    for word in word_bank:
        if target_word.startswith(word):
            suffix_ways = all_construct(target_word[len(word):], word_bank, memo)
            
            target_ways = map(lambda way: [word] + way[:], suffix_ways)
            target_ways = [list(ele) for ele in target_ways]
            total_ways = total_ways + target_ways

    memo[target_word] = total_ways.copy()
    return memo[target_word]


def main():
    arr = all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])
    print(arr)
        # pass


if __name__ == "__main__":
    main()