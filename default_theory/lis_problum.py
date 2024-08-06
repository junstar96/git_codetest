#1. 그냥 동적계획법만 사용했을 때
import bisect

def Lis_1(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

#2, 이진법적 활용을 통해서 좀 더 줄인 방법

def Lis_2(arr):
    n = len(arr)
    if n == 0:
        return n

    tail = [0] * n
    length = 1

    tail[0] = arr[0]

    for i in range(1,n):
        if arr[i] > tail[length - 1]:
            tail[length] = arr[i]
            length+=1
        else: #더 큰 값이 있으면 테일에 추가하고 크지 않다면
            index = bisect.bisect_left(tail,arr[i], 0,length-1)
            tail[index] = arr[i]
    return length

lis = [3,100,15,18,7,4,12,30]

tail = [0] * 8
tail[0] = lis[0]
length = 1

for i in range(1, 8):
    if lis[i] > tail[length - 1]:
        tail[length] = lis[i]
        length+=1
    else:
        index = bisect.bisect_left(tail,lis[i],0,length-1)
        tail[index] = lis[i]
    print(tail)