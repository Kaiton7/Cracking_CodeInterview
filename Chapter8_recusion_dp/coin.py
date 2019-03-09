denomi=[1,5,10,25]
import numpy as np
def Solve(amount, kind ,coins):
    print(coins)
    coins = [0] + coins
    dp = [[0]*(amount+1)]*(kind+1)
    for i in range(amount+1):
        dp[0][i]=1
    for i in range(1,kind):
        for j in range(1,amount):
            dp[i][j]  = dp[i][j-coins[i]]+dp[i-1][j]

    array = np.array(dp)
    print(np.amax(array))
N,M=1000, len(denomi)
Solve(N,M,denomi)
# print(max(dp))