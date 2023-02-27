'''
파일명 : Ex01-LinearSearch.py

선형 검색(Linear Search)
    간단한 검색 알고리즘, 데이터를 처음부터 끝까지
    순차적으로 비교하여 값을 찾는다.
'''

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# 실행코드
arr = [1, 3, 5, 7, 9]
target = 5
result = linear_search(arr, target)
print(result)













