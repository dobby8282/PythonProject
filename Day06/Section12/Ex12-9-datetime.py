'''
파일명 : Ex12-9-datetime.py
datetime 
    날짜와 시간 데이터를 처리할 때 사용한다
'''
import datetime
# 현재 날짜와 시간 변환, 마이크로초 단위 출력
print(datetime.datetime.now())
print(datetime.datetime.today())

# date() 함수 특정날짜를 만들어 반환
print(datetime.date(2023,1,30))
print(datetime.time(10,40,0))

# 날짜 필드값
y = datetime.datetime.now().year
m = datetime.datetime.now().month
d = datetime.datetime.now().day
h = datetime.datetime.now().hour
mi = datetime.datetime.now().minute
s = datetime.datetime.now().second
print('{}년 {}월 {}일 {}:{}:{}'.format(y,m,d,h,mi,s))

# timedlta 날짜/시간 데이터 연산
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
tomorrow = today + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.date(2023,1,30)
date2 = datetime.date(2022,12,24)
print(date1 - date2)
print((date1-date2).total_seconds())
