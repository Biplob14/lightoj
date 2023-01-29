import math


case = int(input())

for i in range(1, case + 1):
    m, n = map(int, input().split())
    if m == 1 or n == 1:
        print(f"Case {i}: {max(m, n)}")
    elif m == 2 or n == 2:
        print("Test: ", int((m*n)/8)*4)
        result = ((int((m*n)/8))*4) + (4 if int((m*n)%8) >= 4 else int((m*n)%8))
        
        print(f"Case {i}: {int(result)}")

    if(m > 2 and n > 2):
        print(f"Case {i}: {math.ceil((m * n) / 2)}")
