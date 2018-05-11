def find_words(word, complete_set):
    matching_words = []
    for w in complete_set:
        if (is_contains(w, word)):
            matching_words.add(w)
    return matching_words

def is_contains(test_word, master_word):
    for c in test_word:
        print(c)
        if (c not in master_word):
            return false
    return true

def __main__():
    complete_set = ['bat', 'trap', 'rat', 'at', 'tab', 'toy']
    word = 'tbla'
    print(find_words(word, complete_set))
