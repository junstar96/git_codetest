k = int(input())

stack_list = list()

def Push(n):
    global stack_list
    stack_list.append(n)

def Pop():
    global stack_list
    data = stack_list[-1]
    del stack_list[-1]
    return data

for i in range(k):
    commend = int(input())
    if commend == 0:
        Pop()
    else:
        Push(commend)

print(sum(stack_list))