'''
파일명 : Ex04-O(nlogn).py

O(n log n)
'''

import time
def merge_sort(arr):
    # 리스트의 길이가 1이하 이면 정령이
    # 이미 끝난 것으로 그대로 반환
    if len(arr) <= 1:
        return arr

    # 리스트 중간 인덱스 계산
    mid = len(arr) // 2

    # 중간을 기준으로 리스트를 두 개로 나누어 각각을 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 두 개의 리스트를 병합하여 정렬된 리스트 생성
    return merge(left, right)

def merge(left, right):
    # 결과를 저장할 리스트 생성
    result = []
    
    # 각각의 리스트에 대해 인덱스를 따로 만들어가며 비교하여 
    # 작은 값을 결과 리스트에 추가
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 아직 추가하지 못한 나머지 값들을 결과 리스트에 추가
    result += left[i:]
    result += right[j:]
    
    # 정렬된 리스트 반환
    return result


for n in range(1, 1000, 10):
    arr = list(range(n))
    target = n - 1
    start_time = time.time()
    result = merge_sort(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("n = {}, result = {}, elapsed_time = {}".format(n, result, elapsed_time))