import sys

list_count = int(input())
dp = [[0 for i in range(3)] for j in range(list_count)]
color_list = [[0 for i in range(3)] for j in range(list_count)]

for i in range(list_count):
    red,blue,green = map(int, sys.stdin.readline().split())
    color_list[i][0] = red
    color_list[i][1] = blue
    color_list[i][2] = green

dp[0][0] = 0
dp[0][1] = 1
dp[0][2] = 2

for i in range(1, list_count):
    for j in range(3):
        if dp[i-1][j] != color_list[i].index(min(color_list[i])):
            dp[i][j] = color_list[i].index(min(color_list[i]))
        else:
            sol = color_list[i][:]
            sol.sort()
            dp[i][j] = color_list[i].index(sol[1])

answer = 1000 * 1001

for i in range(3):
    i_sum = 0
    for j in range(list_count):
        i_sum += color_list[j][dp[j][i]]
    answer = min(answer,i_sum)


print(answer)