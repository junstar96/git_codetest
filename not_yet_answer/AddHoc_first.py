w, h = map(int, input().split())
current_x, current_y = map(int,input().split())
count = int(input())

vec_x = (current_x + count)//w
vec_y = (current_y + count)//h

if vec_x%2==0:
    current_x = (current_x + count) %w
else:
    current_x = w - (current_x + count)%w

if vec_y%2==0:
    current_y = (current_y+count) % h
else:
    current_y = h - (current_y+count) % h


print(current_x,current_y)

#각각의 길이를 직선으로 나눠서 푸는 방법이 있을 줄은 생각치 못했다. 이건 다시 복기하면서 다른 문제도 풀어보자.