'''
파일명 : Ex03-HashTable.py

해시테이블(Hash Table)
    해시 테이블(Hash Table)은 키와 값을 저장하는 데이터 구조로,
    요소의 빠르고 효율적인 검색, 삽입, 삭제를 허용한다.
    해시 함수는 키를 입력으로 받아 값을 저장하거나 검색할 수 있는
    배열 인덱스를 반환한다.
'''
'''
# 사전 생성
d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
'''

def hash_function(key):
    return hash(key) % 10

def insert(hash_table, key, value):
    hash_index = hash_function(key)
    if hash_table[hash_index] is None:
        hash_table[hash_index] = []
    hash_table[hash_index].append((key, value))

def search(hash_table, key):
    hash_index = hash_function(key)
    bucket = hash_table[hash_index]
    if bucket is None:
        return None
    for k, v in bucket:
        if k == key:
            return v
    return None

hash_table = [None] * 10
insert(hash_table, "John Doe", "555-555-5555")
insert(hash_table, "Jane Doe", "555-555-5556")
insert(hash_table, "Jim Doe", "555-555-5557")
insert(hash_table, "KoreaIT", "555-555-5558")

print(search(hash_table, "John Doe"))
print(search(hash_table, "Jane Doe"))
print(search(hash_table, "Jim Doe"))
print(search(hash_table, "KoreaIT"))



