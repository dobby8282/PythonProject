'''
파일명 : Ex06-3-while3.py
'''
my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>> '))
    my_list.append(n)
my_list.pop() # 0 제거
print(my_list)