'''
파일명 : Ex06-O(2^n).py
O(2^n)
'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
