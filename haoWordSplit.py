def wordSplit(dictionary, str):
    check = wordSplitRec(dictionary, str, {})
    # return None if there are no results
    return check[0] if len(check) > 0 else None

def wordSplitRec(dictionary, str, memo):
    # if i've seen this string before
    if str in memo:
        return memo[str]
    # base case
    if str == "":
        return []

    results = []
    # start building results from
    for word in dictionary:
        # if no match for this word, skip
        if str[:len(word)] != word:
            continue
        # if complete match, add to results!
        if len(word) == len(str):
            results.append(word)
        else:
            # word is a match, but still remaining string left
            subResults = wordSplitRec(dictionary, str[len(word):], memo)
            # add possible routes to this str
            for subResult in subResults:
                results.append(word + ' ' + subResult)

    memo[str] = results

    return results

print wordSplit(
    {"a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaab", "aaaaaaaaaaaaaaaaaaaaaaaaaaa"},
    "aaaaaaaaaaaaaaaaaaaaaaaaaaab"
)

# print wordSplit(
#     {"hello", "world", "hellox", "he", "llo", "wo"},
#     "helloxhelloworld"
# )
