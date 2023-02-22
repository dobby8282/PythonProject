'''
Ex08-Graph.py
그래프(Graph)
    노드(vertice)와 간선(정점/edge/arcs)로 이루어진 자료구조.

 A
/ \
B  C
\ /
 D
 |
 E

'''
class Graph:
    def __init__(self, vertices):
        # 생성자 함수, 그래프 객체 생성 시 호출됨
        self.vertices = vertices # 그래프의 정점 리스트
        self.adj_list = {} # 인접 리스트 (해시 테이블)
        for vertex in vertices:
            # 초기화 - 모든 정점의 인접 리스트는 빈 리스트로 설정됨
            self.adj_list[vertex] = []

    def add_edge(self, u, v):
        # 두 정점 사이에 간선 추가
        self.adj_list[u].append(v)  # 정점 u의 인접 리스트에서 v 추가
        self.adj_list[v].append(u)  # 정점 v의 인접 리스트에서 u 추가

    def remove_edge(self, u, v):
        # 두 정점 사이에 간선 제거
        self.adj_list[u].remove(v) # 정점 u의 인접 리스트에서 v 제거
        self.adj_list[v].remove(u) # 정점 v의 인접 리스트에서 u 제거

    def print_graph(self):
        # 그래프 출력
        for vertex in self.vertices:
            print(vertex, end=' -> ')
            print(' -> '.join([str(node) for node in self.adj_list[vertex]]))


vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph(vertices)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.print_graph()




