'''
Ex03-O(n).py

O(n) : 선형 시간 복잡도
'''
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 실행코드
arr = [1, 3, 5, 7, 8]
print(linear_search(arr, 5))
