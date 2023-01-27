'''
파일명 : Ex10-3-method-set.py
'''
# 교집합 intersection()
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 & s2)
result = s1.intersection(s2)
print(result)

# 합집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 | s2)
result = s1.union(s2)
print(result)

# 차집합
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 - s2)
result = s1.difference(s2)
print(result)


