list_count = int(input())
dp = [0] * list_count

for i in range(list_count):
    dp[i] = list(map(int, input().split()))

for i in range(1, list_count):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[list_count-1][0], dp[list_count-1][1], dp[list_count-1][2]))