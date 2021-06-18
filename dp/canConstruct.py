def can_construct(target_word, word_bank, memo = {}):

    if target_word in memo: return memo[target_word]
    if target_word == "": return True
    
    for word in word_bank:
        if target_word.startswith(word):
            if can_construct(target_word[len(word):], word_bank, memo):
                memo[target_word] = True
                return True
    memo[target_word] = False
    return False


def main():
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeeeee']))


if __name__ == "__main__":
    main()