from random import randrange


T = int(input())

for i in range(T):
    r = int(input())
    if r>10:
        print(10, r-10)
    else:
        print(0, r)