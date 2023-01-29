case = int(input())
divisable = 0
for i in range(1, case+1):
    A, B = map(int, input().split())
    seq = ''
    for j in range (1, B+1):
        seq += str(j)
        print("j=", j)
        

    for j in  range(A, B+1):

        print(seq[:j])
        if int(seq[:j]) %3 == 0:
            divisable += 1

    print(divisable)