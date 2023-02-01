'''
파일명 : Ex13-5-readHello2.py
file 객체 read() -> 전체 읽어오기
        read(인자값) -> 인자값 만큼 읽어오기
'''
file = open('hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5)
    if not str: # 읽을 값이 없으면 True
        break
    print(str)
file.close()

