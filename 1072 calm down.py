import math
pi = math.pi

case = int(input())

for i in range(1, case+1):
    R, n = map(float, input().split())
    # R = float(input())

    r = (R*(math.sin(pi/n))) / (1 + math.sin(pi/n))

    print(f"Case {i}: {r:.10f}")