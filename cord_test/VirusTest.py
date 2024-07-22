computer_num = int(input())
computer_pair = int(input())

computer_list = dict()
computer_queue = list()
computer_queue.append(1)
already_virus = set()


for i in range(0, computer_pair):
    key,value = map(int,input().split())
    if key not in computer_list:
        computer_list[key] = list()

    if value not in computer_list:
        computer_list[value] = list()
    computer_list[key].append(value)


while computer_queue:
    check = computer_queue.pop(0)
    already_virus.add(check)

    if check not in computer_list.keys():
        continue

    for i in computer_list[check]:
        if i not in already_virus:
            computer_queue.append(i)

print(already_virus)
print(len(already_virus)-1)

