import sys #c++에서 시간 초과를 해결하기 위해 cin.untie나 여러 가지 앞에 줄 붙이는 것과 같은 느낌
import heapq

test_case = int(input())

heap = []

for i in range(test_case):
    #x = int(input()) : 이러면 시간 초과함
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap,-x)
        print(heap)


