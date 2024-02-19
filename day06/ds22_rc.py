# date : 20240219
# file : ds22.rc.py
# desc : 재귀함수

import time

def open_box():
    global count
    print(f'{count}번째 상자를 엽니다')
    count -= 1
    if count == 0:
        print('반지를 넣고 반환합니다')
        return

    time.sleep(0.1)
    open_box()
    print('상자를 닫습니다')
# 전역변수
count = 10

if __name__ == '__main__':
    open_box()