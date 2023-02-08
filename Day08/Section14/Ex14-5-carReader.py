'''
Ex14-5-carReader.py
'''
import csv

with open('차량관리.csv', 'r', newline='', encoding='UTF-8') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in csv_reader:
        print(line)