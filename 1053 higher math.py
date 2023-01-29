case = int(input())

for i in range(1, case+1):
    a, b, c = map(int, input().split())
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print(f"Case {i}: yes")
    else:
        print(f"Case {i}: no")
