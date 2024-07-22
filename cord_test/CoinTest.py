
def solution(n, k):
    coin_num = n
    value = k
    count = 0

    coin_list = list()
    for i in range(coin_num):
        coin_list.append(int(input()))


    coin_list.reverse()
    for coin in coin_list:
        if value >= coin:
            count += value//coin
            value %= coin


    return count

n,k = map(int,input().split())

print(solution(n,k))