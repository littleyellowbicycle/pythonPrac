def words_break(stuff):
    """this function will break up words for us"""
    words=stuff.split()
    return words

def sort_words(words):
    """this function will sort words"""
    return sort(words)

def print_first_words(words):
    """this function will print the first words after popping it off"""
    word=words.pop(0)
    print word

def last_word_print(words):
    """this function will print the first words after popping it off"""
    word=words.pop(-1)
    print word


def sort_sentence(sentence):
    words=words_break(sentence)
    return sort_words(words)

def print_first_last(sentence):
    words=sort_sentence(sentence)
    print_first_words(words)
    last_word_print(words)