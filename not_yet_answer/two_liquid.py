import sys
test_case = int(input())
riquid_list = sorted(list(map(int,sys.stdin.readline().split())))

left = 0
right = test_case-1


answer = abs(riquid_list[left] + riquid_list[right])
answer_list = [riquid_list[left],riquid_list[right]]

while left < right:
    temp = riquid_list[left] + riquid_list[right]
    if answer > abs(temp):
        answer = abs(temp)
        answer_list = [riquid_list[left],riquid_list[right]]
        if answer == 0:
            break
    if temp < 0:
        left+=1
    else:
        right-=1


print(answer_list[0], answer_list[1])