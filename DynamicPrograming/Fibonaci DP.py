def func_call(n, dp):
    if(n==1 or n==0):
        return n

    if(dp[n-1] == - 1):
        smallans1 = func_call(n - 1, dp)
        dp[n-1] = smallans1
    else:
        smallans1 = dp[n-1]

    if(dp[n-2] == -1):
        smallans2 = func_call(n-2,dp)
        dp[n-2] = smallans2
    else:
        smallans2 = dp[n-2]

    myans = smallans1 + smallans2
    return myans

n = int(input())
dp = [-1 for i in range(n+1)]
ans = func_call(n,dp)
print(ans)