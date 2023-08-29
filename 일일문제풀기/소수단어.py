import math

word = input() # AbCd

total = 0
for w in word:
    if w.lower():
        total += ord(w)
    else:
        total += ord(w)

# 소수 판별
isPrime = True
for i in range (2, math.sqrt(total)+1):
    if total % i == 0:
        isPrime = False
    
if isPrime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")