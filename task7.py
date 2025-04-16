def countConsistentStrings(allowed, words):
    allowed_set = set(allowed)  # Convert allowed string to a set for fast lookups
    count = 0

    for word in words:
        if all(char in allowed_set for char in word):  # Check if word is consistent
            count += 1

    return count

# Example usage:
allowed = "abc"
# allowed="ab"
# allowed="cad"
words = ["a", "b", "c", "ab", "ac", "bc", "abc", "d"]
# words = ["ad","bd","aaab","baa","badab"]
# words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(countConsistentStrings(allowed, words))  
