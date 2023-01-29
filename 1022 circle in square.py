import math
PI = 2.0 * math.acos(0.0)
# print(PI)

case = int(input())

for i in range(1, case+1):
    r = float(input())
    area_of_circle = PI*(r**2)
    area_of_sqr = (r*2)**2
    # print("circle: ", area_of_circle)
    # print("square: ", area_of_sqr)
    shade = area_of_sqr - area_of_circle
    print(f"Case {i}:", float("{:.2f}".format(shade)))