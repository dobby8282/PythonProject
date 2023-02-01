'''
파일명 : Ex13-1-makeFile.py

파일 입출력(I/O - input/output)
    입력(input) 기존 파일 읽어들이는 것
    출력(output) 파일생성, 내용 추가를 말한다.
'''

# file = open('myFile.txt', 'wt')
# print('myFile.txt 파일이 생성되었습니다.')
# file.close()

# with 문 - 자동으로 close()를 해준다.
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')
