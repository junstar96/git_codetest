star_num = int(input())

for i in range(1,star_num):
    print(" "*(star_num -i) + "*"*(2*i - 1))
for i in range(star_num,0,-1):
    print(" "*(star_num- i) + "*"*(2*i - 1))