'''
삽입 정렬(Insertion Sort)
    리스트의 모든 요소를 앞에서부터 차례대로
    이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입

    O(n^2)의 시간복잡도 갖는다.
'''
def insertion_sort(arr):
    n = len(arr)    # 배열의 길이
    # arr = [64, 25, 12, 33, 11, 66]
    # n = 6
    for i in range(1, n):   # 1부터 n-1까지 반복
        key = arr[i]    # 현재 위치의 값을 key 변수에 저장
        #  key : 25    i : arr[1]
        #  key : 12    i : arr[2]

        j = i - 1   # 현재 위치의 이전 위치를 j 변수에 저장
        #  j : 0
        #  j : 1

        #  i:1 True and arr[0]:65 > key:25 True | False
        '''
         i:2 True and arr[1]:65 > key:12 True 
            | True and arr[0]:25 > key:12 True
        '''
        while j >= 0 and arr[j] > key: # 이전 위치부터 첫 번째 위치까지 반복
            # 현재 위치의 값을 이전 위치로 이동
            arr[j+1] = arr[j]
            # i:1 arr[1] = 65
            # i:2 arr[2] = 65 | arr[1] = 25

            j -= 1  # 이전 위치로 이동
            # j: -1
            # j: 0 | j:-1

        arr[j+1] = key  # key 값을 현재 위치에 저장
        # arr[0] = 25
    return arr

# 실행코드
arr = [12, 25, 65, 33, 11, 66]
print(insertion_sort(arr))









