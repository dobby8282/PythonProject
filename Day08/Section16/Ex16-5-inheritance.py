'''
Ex16-5-inheritance.py
상속
    어떤 클래스가 가지고 있는 기능을
    그대로 물려받아 사용할 수 있는 클래스
    
상속방법

class 슈퍼클래스
    본문
    
class 서브클래스(슈퍼클래스)
    본문

'''

# 슈퍼클래스(부모클래스)
class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self):
        print('원두: {}'.format(self.bean))


# 서브클래스(자식클래스)
class Espresso(Coffee):
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info()
        print('물: {}ml'.format(self.water))

coffee = Espresso('콜롬비아', 30)
coffee.espresso_info()

print(coffee.bean)
coffee.coffee_info()

