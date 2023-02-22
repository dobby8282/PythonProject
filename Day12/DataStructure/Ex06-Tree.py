'''
파일명 : Ex06-Tree.py

트리 자료구조
    단 하나의 루트 노드가 있고, 루트 노드에서 하위 노드들이 연결된 비선형 계층구조이다.

이진트리(Binary Tree)
    모든 노드가 최대 2개의 자식 노드를 가질 수 있는 구조를 말한다.
    왼쪽 서브 트리의 값은 루트의 값보다 작고, 오른쪽 서브트리의 값은 루트보다
    큰 값을 가지도록 구성한다.
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarrySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data): # 이진 트리에 데이터를 넣는 부분
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):

        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key): # 이진 트리에서 데이터를 찾는 부분
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key): # 이진 트리에서 데이터를 지우는 부분
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def DFTravel(self ): # 데이터 출력하는 부분
        """
            깊이 우선 탐색 중 전위 순회
            뿌리 > 왼쪽 트리 > 오른쪽 트리
         """
        def _DFTravel(root):
            if root is None:
                pass
            else:
                print(root.data, end=' ')
                _DFTravel(root.left)
                _DFTravel(root.right)
        _DFTravel(self.root)

    def LFTravel(self):
        """
            깊이 우선 탐색 중 중위 순회
            왼쪽 트리 > 뿌리 > 오른쪽 트리
        """
        def _LFTravel(root):
            if root is None:
                pass
            else:
                _LFTravel(root.left)
                print(root.data, end=' ')
                _LFTravel(root.right)
        _LFTravel(self.root)

    def LRTravel(self):
        """
            깊이 우선 탐색 중 후위 순위
            왼쪽 트리 > 오른쪽 트리 > 뿌리 노드
        """
        def _LRTravel(root):
            if root is None:
                pass
            else:
                _LRTravel(root.left)
                _LRTravel(root.right)
                print(root.data, end=' ')
        _LRTravel(self.root)
        
    
    def layerTravel(self):
        """
            너비 우선 탐색
            뿌리 노드부터 깊이 순으로 방문
        """
        def _layerTravel(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data, end=' ')
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
        _layerTravel(self.root)


# 실행코드
data = [20, 6, 8, 12, 78, 32, 65, 7, 9]

tree = BinarrySearchTree()

for x in data:
    tree.insert(x)

print('==DFTravel==')
tree.DFTravel() # 전위 순회
print()

print('==LFTravel==')
tree.LFTravel() # 중위 순회
print()

print('==LRTravel==')
tree.LRTravel() # 후위 순회
print()

print('==layerTravel==')
tree.layerTravel() # 너비 우선 탐색
print()



















