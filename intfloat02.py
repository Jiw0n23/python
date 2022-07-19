# input()의 결과는 문자열
str_input=input("원의 반지름 입력을 입력해 주세요 >")
# str_input을 숫자로 변화해야 연산이 가능. 여기서는 실수형으로 변환함.
num_input=float(str_input)
pi = 3.141592

print()
print("반지름:", num_input)
print("둘레:", 2*3.14*num_input)
print("넓이:", 3.14 * num_input **2)

