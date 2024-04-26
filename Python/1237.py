#getting time limit exceeded
def main():
    while True:
        try:
            str1 = input()
        except EOFError:
            break
        str2 = input()
        m, n = len(str1), len(str2)

        # Create a table to store lengths of longest common suffixes of substrings
        dp = [[0] * (n+1) for _ in range(m+1)]
        result = 0  # To store length of the longest common substring

        # Build dp table in bottom-up manner
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = 0

        print(result)

if __name__ == '__main__':
    main()