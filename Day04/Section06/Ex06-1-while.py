'''
파일명 : Ex06-1-while.py

반복문
    어떤 수행 작업을 한 번이 아니라 계속해서 수행해야 할 때 사용한다.

반복문 종류
    while, for문
    
while문
    특정 조건을 만족하는 동안 반복해서 수행하는 코드
    
while 조건식:
    반복 실행코드

'''
n = 10
while True:
    print(n)
    n -= 1  # n = n - 1 같다

print("while문 끝나고 n의 값 : {}".format(n))

