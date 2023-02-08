'''
파일명 : Ex16-1-constructor.py

생성자
    인스턴스를 생성할 때 생성자가 자동으로 호출된다.
    객체 초기화 용으로 사용한다.

    __init()__
'''
class USB:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print('{}GB USB'.format(self.capacity))

usb = USB(128)
usb.info()

usb2 = USB(1024)
usb2.info()

'''
1bit - 0 또는 1
1byte - 8bit
1kbyte - 1024byte
1mbyte - 1024kbyte
1gbyte - 1024mbyte
1tbyte - 1024gbyte
'''

