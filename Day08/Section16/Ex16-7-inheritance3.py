'''
파일명 : Ex16-7-inheritance3.py
'''

class Car:

    max_oil = 50    # 최대 주유량

    def __init__(self, oil):    # 생성자 - 객체가 생성되기 직전에 실행
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:    # 0 이하의 주유는 진행하지 않음
            return
        self.oil += oil
        if self.oil > Car.max_oil:  # 주유 후 최대 주유량 초과 상태이면
            self.oil = Car.max_oil

    def car_info(self):
        print('현재 주유상태: {}'.format(self.oil))


class Hybrid(Car):

    max_battery = 30

    def __init__(self, oil, battery):
        super().__init__(oil)   #  self.oil = oil 같음
        self.battery = battery

    def charge(self, battery):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()  # print('현재 주유상태: {}'.format(self.oil))
        print('현재 충전상태: {}'.format(self.battery))


car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()










