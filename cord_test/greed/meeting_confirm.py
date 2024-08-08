import sys

meeting = int(input())
test_list = list()

for i in range(meeting):
    x,y = map(int,sys.stdin.readline().split())
    test_list.append((x,y))


test_list.sort(key=lambda x:(x[1],x[0]))


max_meeting_list = list()
max_meeting_list.append(test_list[0])
last_num = max_meeting_list[0][1]

for i in range(1, len(test_list)):
    if last_num <= test_list[i][0]:
        max_meeting_list.append(test_list[i])
        last_num = test_list[i][1]

print(len(max_meeting_list))

