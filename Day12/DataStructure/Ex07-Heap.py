'''
Ex07-Heap.py

힙(Heap)
    최댓값 및 최솟값 찾아내는 연산을 빠르게 하기 위해 고안된 완전이진트리를
    기본으로 한 자료구조  

'''

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)


heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

heap = MaxHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('==MaxHeap==')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())