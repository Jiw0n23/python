output_a = "{:d}" .format(52)

output_b = "{:5d}" .format(52)
output_c = "{:10d}" .format(52)

output_d = "{:05d}" .format(52)
output_e = "{:05d}" .format(-52)

print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)

print("{:+d} => ","{:+d}".format(52))

output_a = 52.0
output_b = "{:g}" .format(output_a)
print(output_a)
print(output_b)

a = "Hello World!"
print(a.upper())


input_a = """
      안녕하세요
문자열의 함수를 알아봅니다
"""
print(input_a.strip())
print(input_a.isspace())

a = "10, 20, 30, 40, 50, 60".split(", ")
print(a)

input_a = """
      안녕하세요
       문자열
        함수를 알아봅니다
"""
print(input_a.strip())


a = input("> 1번째 숫자: ")
b = input("> 2번째 숫자: ")
print()

print("{} + {} = {}" .format(a,b, int(a)+int(b)))