# 시간과 관련된 기능을 가져온다.
import time

# 변수를 선언한다.
number = 0

# 5초 동안 반복한다.

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

# 출력한다.
print("5초 동안 {}번 반복했습니다." .format(number))