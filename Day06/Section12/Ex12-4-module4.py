'''
파일명 : Ex12-4-module4.py

별명 사용하기
'''
import converter as cvt

miles = cvt.kilometer_to_miles(150)
print('150km={}miles'.format(miles))

pounds = cvt.gram_to_pounds(1000)
print('1000g={}pounds'.format(pounds))
