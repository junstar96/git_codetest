import sys

#3면이 계속 확장되게 할 수 있을까?
#s1 = 1, s2 = 1, s3 = 1
#이 문제는 위치 정보를 필요로 하는가?
#

check = [0 for i in range(100)]
check[0] = 1
check[1] = 1
check[2] = 1
check[3] = 2
check[4] = 2
check[5] = 3
check[6] = 4
check[7] = 5
check[8] = 7
check[9] = 9
test_case = int(input())

for i in range(test_case):
    loop = int(sys.stdin.readline())
    if loop < 10:
        print(check[loop-1])
    else:
        for j in range(10, loop):
            check[j] = check[j-1] + check[j-5]
        print(check[loop-1])






