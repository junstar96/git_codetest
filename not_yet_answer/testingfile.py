import sys

test_case = int(input())

#문제 : 지나가는 노드의 종류를 최소화 하라
#같은 노드를 여러 번 지나가도 상관 없다

#이 코드를 좀 기억하도록 하자
def Solve(start, ans,visited,group):
    visited[start] = True
    for i in group[start]:
        if visited[i] == False:
            ans = Solve(i,ans+1, visited,group)
    return ans





for i in range(test_case):
    size,count = map(int, input().split())
    checking_list = [list() for i in range(size+1)]
    set_check = [False for i in range(size+1)]
    set_check[0] = True

    for i in range(count):
        a,b = map(int,sys.stdin.readline().split())
        checking_list[a].append(b)
        checking_list[b].append(a)

    count_of_flight = Solve(1,0,set_check,checking_list)


    print(count_of_flight)