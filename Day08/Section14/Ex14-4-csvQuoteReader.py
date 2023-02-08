'''
파일명 : Ex14-4-csvQuoteReader.py
'''
member_list = []
with open('회원명단.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # 첫줄제거
    while True:
        line = file.readline()
        if not line:
            break
        member = line.split(',')
        member[0] = member[0].strip('"')
        member[2] = member[2].strip('\n')

        member_list.append(member)

print(member_list)
