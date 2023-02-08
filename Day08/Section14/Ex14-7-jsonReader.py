'''
파일명 : Ex14-7-jsonReader.py
'''
import json
with open('dictList.json', 'r', encoding='UTF-8') as file:
    json_reader = file.read()
    dict_list = json.loads(json_reader)

for dic in dict_list:
    print('이름: {}'.format(dic['name']))
    print('나이: {}'.format(dic['age']))
    print('키: {}'.format(dic['spec'][0]))
    print('몸무게: {}'.format(dic['spec'][1]))
    print()
