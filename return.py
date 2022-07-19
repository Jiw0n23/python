# 함수를 선언합니다.

start = int(input("첫 번째 값 > "))
end = int(input("두 번째 값 > "))

def sum_all(start, end):
    # 변수를 선언합니다.
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1):
        output += i
    # 리턴합니다.
    return output

    
# 함수를 호출합니다.
print("숫자 합계:", sum_all(start, end))