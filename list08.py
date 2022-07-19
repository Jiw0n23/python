# 0에서 100 사이의 짝수의 합을 구하시오.
total = 0
for i in range(0, 101):
    if i%2 == 0:
        total += i
print(total)