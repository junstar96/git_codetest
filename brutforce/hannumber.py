n = int(input())

if n < 100:
    print(n)
elif n == 1000:
    print(144)
else:
    answer = 99
    for i in range(100, n+1):
        a = [0] * 3
        a[0] = i//100
        a[1] = (i//10)%10
        a[2] = i%10

        if a[0] - a[1] == a[1] - a[2]:
            print(a)
            answer+=1
    print(answer)