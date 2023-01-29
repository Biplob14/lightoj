# not solver. unknown reason
case =  int(input())


for i in range(1, case+1):
    w = int(input())

    if w % 2 == 0:
        n = int(w/2)
        m = 2

        while n % 2 == 0:
            n /= 2
            m *= 2
        print(f"Case {i}: {int(n)} {int(m)}")
    else:
        print(f"Case {i}: Impossible")
