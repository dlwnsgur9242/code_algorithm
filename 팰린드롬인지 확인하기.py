# 문제
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

# 예제 입력 1 
# level
# 예제 출력 1 
# 1
# 예제 입력 2 
# baekjoon
# 예제 출력 2 
# 0

# ex.1)
n = input("")
m = ""
for i in range(len(n)-1,-1,-1):
    m +=  n[i]
if n == m:
    print(1)
else:
    print(0)


# ex.2)
# n = input("")
# is_palindrome = 1
# for i in range(len(n)//2):
#     if n[i] != n[len(n)-1-i]:
#         is_palindrome = 0
#         break
# print(is_palindrome)