'''
파일명 : Ex04-QuickSort.py

퀵 정렬(Quick Sort)
    분할 정복 알고리즘의 일종, 기준점(pivot)을 설정하고
    pivot보다 작은 값을 왼쪽, 큰 값을 오른쪽으로 분할한 후
    각 부분 리스트에 대해 재귀적으로 퀵 정렬을 수행하는 알고리즘.

    평균적으로 O(nlogn)의 시간 복잡도를 갖는다.
    최악의 경우 O(n^2)
'''

def quick_sort(arr):
    # 재귀 종료 조건: 리스트의 길이가 1 이하일 경우
    if len(arr) <= 1:
        return arr

    # pivot 값 설정
    pivot = arr[0]

    # pivot을 기준으로 left, right, equal 리스트에 나눠 담음
    left, right, equal = [], [], []
    for a in arr:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)

    # 재귀적으로 left, right 부분 리스트에 대해 quick_sort를 수행하고
    # 그 결과를 합침
    return quick_sort(left) + equal + quick_sort(right)

# 실행 코드
arr = [6, 4, 8, 9, 3, 55, 66, 77, 1]
print(quick_sort(arr))

