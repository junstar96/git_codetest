import sys

test_list = [5, 12, 7, 10, 9, 1, 2, 3, 11]

list_count = int(input())
listcheck = sorted(list(map(int,sys.stdin.readline().split())))
test_num = int(input())

answer = 0
left,right = 0, list_count-1

while left < right:
    temp = listcheck[left] + listcheck[right]
    if temp == test_num:
        answer+=1
        left+=1
    elif temp < test_num:
        left+=1
    else:
        right-=1


print(answer)