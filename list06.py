total = 0
for i in range(1,101): 
    binary = "{:b}".format(i)
    if binary.count("0") == 1:
        print(i, ":", binary)
        total += i

print("합계:", total)