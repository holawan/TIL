# 실습문제 4.3.2
# 사용자로부터 태어난 연도를 입력받고,
# 현재 나이를 출력하기

birth = int(input("태어난 연도를 입력해주세요>>>"))

from datetime import datetime

now = datetime.now().year
print(now-birth)