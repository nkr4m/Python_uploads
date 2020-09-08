import sys

def minsstepto1(n,dp):
    if(n == 1):
        return 0

    minstep2 = sys.maxsize
    if(n%2 == 0):
        if(dp[n//2] == -1):
            minstep2 = minsstepto1(n//2, dp)
            dp[n//2] = minstep2
        else:
            minstep2 = dp[n//2]


    minstep3 = sys.maxsize
    if(n%3 == 0):
        if(dp[n//3] == -1):
            minstep3 = minsstepto1(n//3, dp)
            dp[n//3] = minstep3
        else:
            minstep3 = dp[n//3]

    if(n>0):
        if(dp[n-1] == -1):
            minstep1 = minsstepto1(int(n-1), dp)
            dp[n-1] = minstep1
        else:
            minstep1 = dp[n-1]
    return 1 + min(minstep1, minstep2, minstep3)
n = int(input())
dp = [-1 for i in range(n)]
ans=  minsstepto1(n,dp)
print(ans)