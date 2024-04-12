import math

def mcm(lst):
    n = len(lst)-1
    
    dp = [[-1]*n for i in range(n)]

    def helper(i, j):
        if i >= j:
            return 0
    
        if dp[i][j] != -1:
            return dp[i][j]
        
        dp[i][j] = math.inf
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j],
                helper(i, k) + helper(k+1, j) + lst[i-1]*lst[k]*lst[j]
            )

        return dp[i][j]
        
    print(dp)
    return helper(1, n-1)

lst = [1, 2, 3]
if __name__ == '__main__':
    print(mcm(lst))