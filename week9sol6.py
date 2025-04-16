def minDistance(word1, word2):
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: word1 to empty and empty to word2
    for i in range(m + 1):
        dp[i][0] = i  # delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # insert all characters

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # same char, no cost
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # delete
                    dp[i][j - 1],     # insert
                    dp[i - 1][j - 1]  # replace
                )

    return dp[m][n]
# Example 1
word1 = "horse"
word2 = "ros"
print("Output 1:", minDistance(word1, word2))  # Output: 3

# Example 2
word1 = "intention"
word2 = "execution"
print("Output 2:", minDistance(word1, word2))  # Output: 5
