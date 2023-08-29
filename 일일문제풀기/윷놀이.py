import sys
# 0이 배, 1이 등
a=[]
for i in range(3):
    n = list(map(int, sys.stdin.readline().split(" ")))
    a.append(sum(n))

for i in range(3):
    if a[i]==4:
        print("E")
    elif a[i]==3:
        print("A")
    elif a[i]==2:
        print("B")
    elif a[i]==1:
        print("C")
    else:
        print("D")


# 입력 
# 0 1 0 1
# 1 1 1 0
# 0 0 1 1

# 출력
# B
# A
# B