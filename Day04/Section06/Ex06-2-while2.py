'''
파일명 : Ex06-2-while2.py
'''
my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
print(my_list)
