case = int(input())

for i in range(1, case + 1):
    x1, y1, x2, y2 = map(int, input().split())
    m = int(input())

    print(f"Case {i}:")
    while m:
        x, y = map(int, input().split())
        if x>x1 and x<x2 and y>y1 and y<y2:
            print("Yes")
        else:
            print("No")

        m -= 1