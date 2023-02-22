'''
파일명 : Ex02-SelectionSort.py
    주어진 리스트에서 최소값을 찾아 맨 앞에 있는 값과 교체하는 알고리즘
    O(n^2)의 시간 복잡도
'''
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr