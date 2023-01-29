case = int(input())
for e in range(1, case+1):
    n = int(input())
    res = 0
    while n:
        res += n % 2
        n = n // 2
        
    st = ""
    if res%2==0:
        st = "even"
    else:
        st = "odd"

    print(f"Case {e}: {st}")
