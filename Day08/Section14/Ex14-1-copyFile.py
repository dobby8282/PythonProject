'''
파일명 : Ex14-1-copyFile.py

파일복사
    원본 -> 버퍼 변수(Memory) -> 복사본

b(binary mode) : 해당 파일의 데이터를 바이너리 파일로 인식하고 입출력.

'''
buffer_size = 1024  # 1024byte -> 1KB 의미
with open('../../Day07/Section13/hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
print('hello2.txt 파일이 복사 되었습니다.')