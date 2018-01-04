import string

def reverseWords(stringIn):
    words = filter(lambda x: x != "", string.split(stringIn, ' '))

    return string.join(words[::-1], ' ').strip()

assert(reverseWords("the quick brown fox jumped over the lazy dog") == "dog lazy the over jumped fox brown quick the")
assert(reverseWords("") == "")
assert(reverseWords(" ") == "")
assert(reverseWords("b     a    ") == "a b")
