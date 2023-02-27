'''
파일명 : Ex06-HeapSort.py
힙정렬(Heap Sort)
    최대/최소 힙(heap) 자료구조를 이용하여 배열을 정렬하는 알고리즘
    O(nlogn) 시간복잡도를 가진다.

'''

import heapq

def heap_sort(arr):
    h = []
    for value in arr:
        heapq.heappush(h, value)    # 힙에 원소 추가

    # 힙에서 원소를 꺼내 정렬된 리스트 반환
    return [heapq.heappop(h) for i in range(len(h))]

# 실행코드
arr = [4, 10, 3, 5, 1]
print(heap_sort(arr))













