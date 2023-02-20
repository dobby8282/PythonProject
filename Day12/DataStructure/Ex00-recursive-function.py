'''
파일명 : Ex00-recursive-function.py
재귀함수
    하나의 함수가 실행되는 동안 자신을 다시 호출하는 함수.
'''

def countdown(n):
    if n <= 0:
        print('발사!')
    else:
        print(n)
        countdown(n-1)

countdown(3)