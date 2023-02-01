'''
파일명 : Ex13-4-readHello1.py

r (read mode) : 읽기 전용 모드 / 파일 없으면 에러

경로
    절대경로 예) C://pstudy//PythonProject//Day07//Section13//hello.txt
    상대경로 예) /hello2.txt
                ../../resources/hello.txt
        . -> 현재폴더
        .. -> 상위폴더
    최상위 경로(root) / 또는 C:/(윈도우OS)
'''
file = open('/hello5.txt', 'rt')
str = file.read()
print(str, end='')
file.close()

print()
# with open('hello.txt', 'rt') as file:
#     str = file.read()
#     print(str, end='')




