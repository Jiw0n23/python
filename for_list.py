array = [273, 32, 103, 57, 52]
i=0

for element in array:
    print(element)
    print(element*2)

    element = element * 2
    array[i] = element
    i += 1

    print(array)
print()

for char in "여기는 한국정보교육원입니다":
    print('*', char)