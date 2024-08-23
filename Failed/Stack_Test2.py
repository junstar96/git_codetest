import sys

stack = list()

def StackCommend():
    num = sys.stdin.readline().split()
    global stack
    if num[0] == '1':
        stack.append(int(num[-1]))
    elif num[0] == '2':
        if stack:
            print(-1)
        else:
            check = stack.pop()
            print(check)
    elif num[0] == '3':
        print(len(stack))
    elif num[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

test_case = int(sys.stdin.readline())
for i in range(test_case):
    StackCommend()