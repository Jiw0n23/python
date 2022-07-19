#total = 0
#for i in range(0, 101):
#    octal = "{:o}" .format(i)
#    if octal.count("0") == 1:
#        print(i, ":", octal)
#        total += i
#print("합계: ", total)
#print()

total = 0
# print([i for i in range(0, 101) if "{:0}" .format(i).count("0") == 1])
output = [i for i in range(0, 101) if "{:o}" .format(i).count("0") == 1]
for i in output:
   print("{} : {} ".format(i, "{:o}".format(i)))
print("합계: ", sum(output))

print()

total = 0
# print([i for i in range(0, 101) if "{:o}" .format(i).count("0") == 1])
output = [i for i in range(0, 101) if "{:b}" .format(i).count("0") == 1]
for i in output:
   print("{} : {} ".format(i, "{:b}".format(i)))
print("합계: ", sum(output))