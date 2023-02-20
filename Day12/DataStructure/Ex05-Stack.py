'''
파일명 : Ex05-Stack.py

스택(Stack)
    한 쪽 끝에서만 자료를 넣거나 뺄 수 있는 선형 구조로
    후입선출(LIFO - Last In First Out)로 되어 있다.
    자료를 넣는 것을 '밀어 넣는다' 하여 푸쉬(push)라고 하고
    반대로 넣어둔 자료를 꺼내는 것을 팝(pop) 이라고 하는데,
    이때 꺼내지는 자료는 가장 최근에 푸쉬한 자료부터 나오게 된다.
'''

def Stack():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    print(stack)

    while stack:
        print("POP Value is :", stack.pop())

Stack()