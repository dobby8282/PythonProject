'''
파일명 : Ex13-9-readHello6.py
'''

import sys

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list)