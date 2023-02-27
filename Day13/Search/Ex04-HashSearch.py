'''
파일명 : Ex04-HashSearch.py

해시 검색(Hash Search)
    해시 테이블(Hash Table)을 이용하여 데이터를 검색하는 방법.
    해시 테이블은 Key : Value 구성된 데이터를 저장하는 자료구조
    키를 이용 값을 빠르게 검색할 수 있다.

'''

class HashTable:
    def __init__(self, size):
        self.size = size

        # 빈 리스트를 size 개 만큼 생성하여 2차원 리스트 초기화
        self.hash_table = [[] for _ in range(self.size)]

    def hash_func(self, key):
        return key % self.size  # 나눗셈 해시 함수를 이용하여 키의 해시값을 계산

    def insert(self, key, value):
        hash_value = self.hash_func(key)  # 해시 함수를 이용하여 키의 해시값 계산
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:  # 이미 같은 키가 존재하는 경우
                self.hash_table[hash_value][i][1] = value  # 값을 업데이트하고 반환
                return
        self.hash_table[hash_value].append([key, value])  # 새로운 키와 값을 추가

    def search(self, key):
        hash_value = self.hash_func(key)  # 해시 함수를 이용하여 키의 해시값 계산
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:  # 해당 키가 존재하는 경우
                return self.hash_table[hash_value][i][1]  # 값을 반환
        return None  # 해당 키가 존재하지 않는 경우 None 반환

    def delete(self, key):
        hash_value = self.hash_func(key)  # 해시 함수를 이용하여 키의 해시값 계산
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:  # 해당 키가 존재하는 경우
                del self.hash_table[hash_value][i]  # 해당 키와 값을 삭제하고 True 반환
                return True
        return False  # 해당 키가 존재하지 않는 경우 False 반환

# 실행코드

# 해시 테이블을 생성한다
hash_table = HashTable(10)

# 원소를 해시 테이블에 삽입한다
hash_table.insert(1, "apple")
hash_table.insert(2, "banana")
hash_table.insert(3, "cherry")

# 원소를 해시 테이블에서 검색한다
result1 = hash_table.search(1)
result2 = hash_table.search(2)
result3 = hash_table.search(3)
print(result1, result2, result3)  # "apple" "banana" "cherry"
