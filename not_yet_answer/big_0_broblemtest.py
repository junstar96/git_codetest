#상수 c, a0이 주어지고 f(n)은 a1*n + a0의 형태로 진행된다.
#n > n0의 조건이 맞춰지면 f(n) <= c * n의 형태가 되는지를 살펴

a1, a0 = map(int,input().split()) # -100 < a0<a1<100
c = int(input())
n0 = int(input())

#fx = a1 * n + a0

answer = 1

for i in range(n0, 101):
    fx = a1 * i + a0
    gx = i * c
    if fx > gx:
        answer = 0
        break

print(answer)