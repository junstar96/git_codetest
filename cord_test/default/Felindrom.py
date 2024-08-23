wordcheck = str(input())

first_word = str()
last_word = str()

cut_int = len(wordcheck)


if len(wordcheck)%2 == 1:
    first_word = wordcheck[:cut_int//2+1]
    last_word = wordcheck[cut_int//2:cut_int]
else:
    first_word = wordcheck[:cut_int // 2+1]
    last_word = wordcheck[cut_int // 2-1:cut_int]

last_word = last_word[::-1]


if first_word == last_word:
    print(1)
else:
    print(0)
