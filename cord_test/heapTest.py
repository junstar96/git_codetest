import sys #c++에서 시간 초과를 해결하기 위해 cin.untie나 여러 가지 앞에 줄 붙이는 것과 같은 느낌
import heapq

test_case = int(input())

class heap_min_max:

    def __init__(heap_check):
        heap_check.heap_min = []
        heap_check.heap_max = []

    def push_min(heap_check, n):
        heapq.heappush(heap_check.heap_min, n)


    def push_max(heap_check,n):
        heapq.heappush(heap_check.heap_max, -n)


    def pop_min(heap_check):
        check = heapq.heappop(heap_check.heap_min)
        return check

    def pop_max(heap_check):
        check = -heapq.heappop(heap_check.heap_max)
        return check

    def len_max(heap_check):
        return len(heap_check.heap_max)

    def len_min(heap_check):
        return len(heap_check.heap_min)

    def print_max(heap_check):
        print(heap_check.heap_max)

checking = heap_min_max()

for i in range(test_case):
    x = int(sys.stdin.readline())

    if x == 0:
        if checking.len_max() == 0:
            print(0)
        else:
            print(checking.pop_max())
    else:
        checking.push_max(x)
        checking.print_max()