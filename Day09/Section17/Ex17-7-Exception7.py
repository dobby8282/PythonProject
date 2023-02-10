'''
파일명 : Ex17-7-Exception7.py
'''

class HourError(Exception):
    def __init__(self):
        super().__init__('올바른 시간이 아닙니다.')

try:
    hour = int(input('시간을 입력하세요 >>> '))
    if hour < 0 or hour > 23:
        raise HourError
except HourError as e:
    print(e)
