'''
파일명 : Ex05-MergeSort.py

병합 정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각ㄱ을 재귀적으로 합병 정렬을 하고,
    다시 합치면서 정렬하는 알고리즘

    O(nlonn)의 시간복잡도를 갖는다.
'''

def merge_sort(arr):
    # 만약 리스트의 길이가 1이하이면 정렬이
    # 이미 끝난 것이므로 그대로 반환
    if len(arr) <= 1:
        return arr

    # 리스트의 중간 인덱스를 계산
    mid = len(arr) // 2

    # 중간을 기준으로 리스트를 두 개로 나누어 각각을 재귀적으로 정렬
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 두 개의 리스트를 병합하여 정렬된 리스트 생성
    return merge(left, right)

def merge(left, right):
    # 결과를 저장할 리스트를 생성
    result = []

    # 각각의 리스트에 대해 인덱스를 따로 만들어가며 비교하여 작은값을
    # 결과 리스트에 추가
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















