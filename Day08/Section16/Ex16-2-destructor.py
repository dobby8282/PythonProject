'''
파일명 : Ex16-2-destructor.py
소멸자
    인스턴스가 소멸될 때 자동으로 호출된다.
'''
class Service:
    def __init__(self, service=None):
        self.service = service
        print('{} Service가 시작되었습니다.'.format(self.service))

    def __del__(self):
        print('{} Service가 종료되었습니다.'.format(self.service))


s = Service('길 안내')
del s

s2 = Service('커피 주문')

print('프로그램 종료!')


