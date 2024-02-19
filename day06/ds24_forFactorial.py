# file : ds24_forFactorial.py
# desc : 반복문으로 팩토리얼 구하기

factValue = 1
n = 1000

for i in range(10, 0, -1): # 10부터 1까지 역순으로
    factValue *= i

print(f'10x9x8x7x...x2x1 ={factValue}')

# 재귀호출 factorial
def factorial(num):
    if num <= 1: return 1

    return num * factorial(num - 1)

print(f'{n}! = {factorial(n)}')
# n = 1000 하면 RecursionError: maximum recursion depth exceeded 이런 에러 뜸. 재귀호출 최고 깊이를 초과
# 재귀가 간단하긴하지만 성능면에서 좋지 않다