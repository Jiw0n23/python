def mul(*values):
    mul = 1
    for value in values:
            
        mul *= value
    return mul
print(mul(5, 7, 9, 10))