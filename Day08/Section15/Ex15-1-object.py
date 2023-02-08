'''
파일명 : Ex15-1-object.py

클래스
    객체를 만드는 설계도
    붕어빵 틀, 와플 기계
    객체화(인스턴스화) - 메모리에 올리는것
    
객체(object)
    현실 세계 존재하는 물리적, 추상적 식별할 수 있는 모든것.
    예) 컴퓨터, 학생, 주문, 배송

객체 구성
    초기화용 - 생성자
    속성 값 - 변수
    기능 - 메소드(함수)
'''
# Computer 클래스 정의
class Computer:

    # 첫번째 매개변수가 self 이므로 인스턴스 메소드 이다.
    # self를 제외한 나머지 매개변수에 실제로 상용될 데이터가 전달된다.
    def set_spec(self, cpu, ram, vga, ssd): # 'i7', '16GB', 'GTX3060', '512GB'
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd

    def hardware_info(self):
        print('CPU = {}'.format(self.cpu))
        print('RAM = {}'.format(self.ram))
        print('VGA = {}'.format(self.vga))
        print('SSD = {}'.format(self.ssd))

desktop = Computer()    # Computer 객체화(객체생성)
desktop.set_spec('i7', '16GB', 'GTX3060', '512GB')
desktop.hardware_info()
print()
desktop.cpu = 'i9'
desktop.hardware_info()

print()
macbook = Computer()
macbook.set_spec('M2', '16GB', 'M2', '512GB')
macbook.hardware_info()


lggram = Computer()
lggram.set_spec('i5', '16GB', '내장VGA', '512GB')
lggram.hardware_info()

print(type(desktop))
print(type(macbook))
print(type(lggram))


str1 = "안녕하세요"
str2 = "안녕못해요"
print(type(str1))
print(type(str2))





