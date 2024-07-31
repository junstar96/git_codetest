list_size = int(input())

def count_way(value):
    if value == 0:
        return 0
    if value == 1:
        return 1
    if value == 2:
        return 2

    dp = [0] * (value + 1)

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, value+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[value]


print(count_way(list_size))