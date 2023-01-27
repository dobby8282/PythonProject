'''
파일명 : Ex09-3-enumerate.py

enumerate()
    List, Tuple, String 등 자료형을 입력받으면
    인덱스 값을 포함하는 enumerate 객체를 돌려준다.
'''
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(len(months))

for month, day in enumerate(months):
    print('{}월 = {}일'.format(month+1, day))

