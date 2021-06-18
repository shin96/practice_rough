def count_construct(target_word, word_bank, memo = {}):

    if target_word in memo: return memo[target_word]
    if target_word == "": return 1
    total_count = 0
    for word in word_bank:
        if target_word.startswith(word):
            count_for_prefix = count_construct(target_word[len(word):], word_bank, memo)
            total_count += count_for_prefix
    memo[target_word] = total_count
    return memo[target_word]


def main():
    print(count_construct('skateboard', ['s', 'board', 'kate', 'kate']))


if __name__ == "__main__":
    main()