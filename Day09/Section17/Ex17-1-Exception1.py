'''
파일명 : Ex17-1-Exception1.py
'''
a = int(input('제수를 입력하세요 >>> '))
b = int(input('피제수를 입력하세요 >>> '))

print('{} / {} = {}'.format(a, b, a / b))

if b == 0:
    print('0으로 나누는 것은 불가능 합니다.')
else:
    print('{} / {} = {}'.format(a, b, a / b))
