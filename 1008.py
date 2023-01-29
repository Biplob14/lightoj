from math import sqrt
from math import ceil

case = int(input())
# i = 1

for i in range(1, case+1):
    time = int(input())

    root = ceil(sqrt(time * 1.0))
    r = root*root-time

    if r < root:
        y = r + 1
        x = root
    else:
        x = time - (root - 1) * (root - 1)
        y = root

    if(root & 1):
        x, y = y, x

    print(f"Case {i}: {x} {y}")