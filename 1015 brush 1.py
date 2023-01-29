case = int(input())

for i in range(1, case+1):
    z = input()
    N = int(input())
    lst = [int(x) for x in input().split()]
    dst = 0
    for j in lst:
        if j > 0:
            dst += j

    print(f"Case {i}: {dst}")