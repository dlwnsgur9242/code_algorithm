import sys

n = int(sys.stdin.readline())

tree = []
for i in range(n):
    tree.append(int(sys.stdin.readline()))

# 가로수의 간격을 구하기 위해 인접한 가로수들 간의 차이를 계산합니다.
differences = []
for i in range(1, n):
    differences.append(tree[i] - tree[i - 1])

# 차이들의 최대 공약수를 구합니다.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 최대 공약수를 활용하여 가로수를 추가로 심어야 하는 최소 수를 계산합니다.
result = differences[0]

for diff in differences:
    result = gcd(result, diff)
print(tree)
print(max(tree))
print(tree[0])

13 // 2 - 4 + 1
6 - 4 